# 14-Day GenAI Engineer Client Interview Preparation Plan

**Target:** GenAI Engineer — Cognizant India client interview  
**Duration:** 14 days  
**Daily commitment:** 2 hours  
**Total preparation time:** 28 hours  
**Approach:** Rotational learning — cover Python, GenAI/RAG, agents, and backend/system design every day. Week 2 revisits the same areas at a deeper, production-focused level.

---

## Daily Schedule (120 minutes)

| Activity | Time |
|---|---:|
| Python / coding problem | 20 minutes |
| GenAI / RAG | 30 minutes |
| Agents / LangGraph / MCP | 25 minutes |
| AWS / backend / system design | 25 minutes |
| Interview questions and revision | 20 minutes |
| **Total** | **120 minutes** |

Use the final 20 minutes to explain concepts aloud, answer scenario-based questions, and note gaps to revisit.

---

## Week 1 — Fundamentals Across All Sections

| Day | Python / Coding | GenAI / RAG | Agents / LangGraph / MCP | AWS / Backend / System Design | Practical Coding Task |
|---|---|---|---|---|---|
| **1** | Lists, dictionaries, exceptions | RAG architecture and ingestion pipeline | Agent vs. workflow; tool calling | FastAPI endpoints and Pydantic | Build a document parser with error handling. |
| **2** | `async`/`await` and generators | Chunking, overlap, and metadata | LangGraph state and nodes | AWS Bedrock model invocation | Implement chunking and call an LLM. |
| **3** | Functions, decorators, and type hints | Embeddings and vector similarity | Conditional routing in LangGraph | REST APIs and HTTP error handling | Create embeddings and run a similarity search. |
| **4** | Pytest and mocking | Vector databases and top-K retrieval | Tool schemas and structured outputs | Retries, backoff, and timeouts | Build a retrieval function with unit tests. |
| **5** | Concurrency and `asyncio` | BM25, hybrid search, and RRF | MCP client/server fundamentals | Redis and caching | Combine keyword and vector retrieval results. |
| **6** | JSON, files, and data validation | Reranking and retrieval evaluation | Memory and checkpoints | Docker and environment configuration | Rerank results and measure Recall@K or MRR. |
| **7** | Python coding challenge | Prompt construction and citations | Tool failures and fallback routing | System design: document QA service | Explain and test the complete retrieval-to-answer flow. |

### Week 1 checkpoint

By the end of Day 7, aim to:
- [ ] Explain the end-to-end RAG pipeline.
- [ ] Parse, chunk, embed, and retrieve documents.
- [ ] Explain hybrid search and reranking.
- [ ] Build a basic FastAPI endpoint and test it.
- [ ] Explain LangGraph state, nodes, edges, and conditional routing.

---

## Week 2 — Production Readiness and Interview Practice

| Day | Python / Coding | GenAI / RAG | Agents / LangGraph / MCP | AWS / Backend / System Design | Practical Coding Task |
|---|---|---|---|---|---|
| **8** | Custom exceptions and input validation | RAG quality failures and retrieval debugging | Supervisor and multi-agent patterns | IAM, secrets, and access control | Handle empty retrieval and malformed model responses. |
| **9** | Async API design and streaming | Grounded generation and hallucination reduction | Tool selection and argument validation | Bedrock throttling and retries | Implement grounded answers with citations and fallback. |
| **10** | Unit vs. integration testing | Recall@K, MRR, and NDCG | LangGraph cycles and conditional edges | LangSmith tracing and observability | Evaluate a fixed retrieval dataset and inspect failures. |
| **11** | Performance profiling | Semantic caching and cache invalidation | Session memory and checkpoint persistence | Latency, token usage, and cost | Measure response latency with and without caching. |
| **12** | Python data structures and coding practice | Fine-tuning vs. RAG; LoRA and quantization | Prompt injection and agent guardrails | Docker and production deployment | Test malicious documents and unauthorized tool use. |
| **13** | Debug a failing Python API | PDFs, OCR, tables, and metadata filtering | MCP integration and tool errors | Scalability and multi-tenant RAG design | Debug a simulated ingestion or retrieval failure. |
| **14** | Timed Python problem | Explain end-to-end RAG architecture | Explain agent architecture and trade-offs | Client interview simulation | Walk through your project and answer scenario questions aloud. |

### Week 2 checkpoint

By the end of Day 14, aim to:
- [ ] Explain how to evaluate and troubleshoot RAG quality.
- [ ] Implement grounded responses, citations, and fallbacks.
- [ ] Explain agent safety, tool authorization, and prompt-injection defenses.
- [ ] Discuss Bedrock failures, retries, caching, latency, and cost.
- [ ] Present your project architecture and defend key design choices.

---

## Recommended Capstone

Build one **production-oriented RAG + Agent API** throughout the 14 days instead of creating unrelated exercises.

**Suggested stack**
- Python and FastAPI
- LangChain and LangGraph
- AWS Bedrock
- ChromaDB or Pinecone
- Pytest
- LangSmith
- Docker
- Optional: Redis for caching

### Capstone checklist

- [ ] Document ingestion, parsing, chunking, and metadata
- [ ] Embedding generation and vector retrieval
- [ ] Hybrid search, reranking, and retrieval evaluation
- [ ] Bedrock generation with grounded citations
- [ ] FastAPI endpoints and Pydantic validation
- [ ] Agent routing, tools, state, and memory
- [ ] Retries, caching, authentication, and authorization
- [ ] Unit tests, tracing, latency, and cost measurements
- [ ] Docker setup and README with an architecture diagram

---

## Must-Practice Interview Questions

1. Why choose hybrid search over vector search alone?
2. How would you improve a RAG system with poor retrieval recall?
3. What is the difference between an agent and a deterministic workflow?
4. How do you prevent an agent from executing unauthorized tools?
5. How would you reduce LLM latency and cost without significantly reducing answer quality?
6. How do you handle Bedrock throttling, timeouts, and model failures?
7. How do you evaluate hallucinations and citation correctness?
8. How would you debug an agent that selects the wrong tool?
9. How would you design a multi-tenant RAG system with document-level access control?
10. Explain your project architecture, design trade-offs, and one difficult bug you fixed.

---

## Study Rules

1. **Code every day.** Produce a working implementation or a clearly documented failing test.
2. **Keep theory focused.** Learn enough to explain the concept, its alternatives, and its trade-offs.
3. **Test edge cases.** Include empty results, malformed inputs, timeouts, and dependency failures where relevant.
4. **Maintain one Git repository.** Keep daily code, tests, and brief notes together.
5. **Practice explaining aloud.** Client interviews assess reasoning and communication, not just definitions.
6. **Prioritize production judgment.** Be ready to explain why a design was chosen, what failed, and how improvement was measured.

**Success criterion:** After 28 hours, you should be able to demonstrate a small working RAG/agent service and explain its architecture, testing, failure handling, security, and performance trade-offs.
