from langchain_text_splitters import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer 

tokenizer = AutoTokenizer.from_pretrained(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def fixed_size(text: str, chunk_size: int):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(fixed_size(text, chunk_size=10))

text = """
Amazon Bedrock provides access to foundation models.

Applications can use Bedrock for RAG and agent workflows.

Production applications should implement retries for throttling.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separators=["\n\n", "\n", ". ", " "],
     length_function=len,
)

chunks = splitter.split_text(text)

for index, chunk in enumerate(chunks):
    print(f"Chunk: {index}: {chunk}")

def token_count(text: str) -> int:
    return len(tokenizer.encode(text, add_special_tokens=False))

token_spiltter= RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separators=["\n\n", "\n", ". ", " "],
     length_function=token_count,
)