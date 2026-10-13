from pydantic import BaseModel

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

class AgentState(BaseModel):
    query: str
    documents: list[str]
    enough_context: bool
    used_fallback: bool
    answer: str

KNOWLEDGE_BASE = [
    "For throttling errors, use exponential backoff with jitter.",
    "Respect the Retry-After header when the service provides it.",
    "Bound retry attempts and configure request timeouts.",
]

def retrieve_docs(state: AgentState) -> dict:
    query_words = set(state["query"].lower().split())

    docs = [document for document in KNOWLEDGE_BASE if query_words.intersection(document.lower().split())]
    return {"documents": docs}

def grade_context(state: AgentState) -> dict:
    enough_context = len(state["documents"]) > 0
    return {"enough_context": enough_context}

def route_after_grade(state: AgentState) -> dict:
    if state["enough_context"]:
        return "generate"

    return "fallback"

def fallback_search(state: AgentState) -> dict:
    """Simulate a broader fallback retrieval."""
    fallback_documents = [
        "If a request fails temporarily, use bounded retries with backoff."
    ]

    return {
        "documents": fallback_documents,
        "used_fallback": True,
        "enough_context": bool(fallback_documents),
    }

def generate_answer(state: AgentState) -> dict:
    if not state["documents"]:
        answer = (
            "I could not find supporting information. "
            "Please consult the relevant documentation."
        )
    else:
        evidence = "\n".join(
            f"- {document}" for document in state["documents"]
        )

        answer = (
            f"Question: {state['query']}\n"
            f"Answer based on retrieved evidence:\n{evidence}"
        )

    return {"answer": answer}


def build_grapgh():
    builder = StateGraph(AgentState)

    builder.add_node("retrieve_docs", retrieve_docs)
    builder.add_node("grade_context", grade_context)
    builder.add_node("route_after_grade", route_after_grade)
    builder.add_node("fallback_search", fallback_search)
    builder.add_node("generate_answer", generate_answer)

    builder.add_edge(START, "retrieve_docs")
    builder.add_edge("retrieve_docs", "grade_context")
    builder.add_conditional_edges("grade_context", route_after_grade,{
        "generate_answer": generate_answer,
        "fallback_search": fallback_search
    })
    builder.add_edge("fallback_search", "generate_answer")
    builder.add_edge("generate_answer", END)

    checkpointer = InMemorySaver()
    return builder.compile(checkpointer=checkpointer)

if __name__ == "__main__":
    app = build_grapgh()

    config = {
    "configurable": {
        "thread_id": "conversation-001"
    }
}

    result = app.invoke(
    {
        "query": "How should I handle throttling errors?",
        "documents": [],
        "enough_context": False,
        "used_fallback": False,
        "answer": "",
    },
    config=config,
     stream_mode="updates",
)
#With stream_mode="updates", LangGraph emits node updates as execution proceeds. Exact output depends on which nodes execute and which state fields they return.
print(result["answer"])