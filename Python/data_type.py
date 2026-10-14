from functools import wraps
from time import perf_counter
# A list is an ordered, mutable collection that allows duplicate values and can store elements of different data types.
chunks = ["RAG introduction", "Embeddings", "RAG introduction"]

chunks.append("Vector search")


for chunk in chunks:
    print(chunk)

print("After removing duplicates:")
for chunk in chunks[::-1]:
    print(chunk)
#Operation	Example	Purpose
#Access	items[0]	Get first element
#Negative index	items[-1]	Get last element
#Slicing	items[:2]	Get first two elements
#Append	items.append(x)	Add one element
#Extend	items.extend(other)	Add multiple elements
#Remove	items.remove(x)	Remove first matching value
#Pop	items.pop()	Remove and return an element
#Sort	items.sort()	Sort the original list
#Comprehension	[x for x in items]	Create a list from an iterable

print(chunks[:2])

scores = [90, 85, 78, 92, 88]

relevant = [score for score in scores if score >=90]

metadata = {
    "file_name": "guide.pdf",
    "page": 3,
    "chunk_id": "c-103"
}

for key, value in metadata.items():
    print(key, value)

#.keys() — keys
#.values() — values
#.items() — key-value pairs
#.update(other) — add or overwrite entries
#.pop(key) — remove and return a value
#key in dictionary — test whether a key exists

score = result.get("score", 0) # 0 is the default value if "score" key is not found

def greet(name: str) -> str:  # name is a parameter
    return f"Hello, {name}"


print(greet("Engineer"))  # "Engineer" is an argument

def create_prompt(query: str, max_token: int) -> str:
    return (
        f"Query: {query}\n"
    )

# Use *args for a variable number of positional arguments and **kwargs for a variable number of keyword arguments.
# *args collects all positional arguments into a tuple.
# *args → accepts multiple positional arguments.
# **kwargs → accepts multiple keyword arguments.
# **kwargs collects keyword arguments into a dictionary.
def total_tokens(*token_counts: int) -> int:
    return sum(token_counts)


def model_config(**settings: object) -> dict[str, object]:
    return settings


print(total_tokens(100, 200, 50))
print(model_config(model="example-model", temperature=0.1))

def measure_time(func):
    @wraps(func) #It preserves important metadata from the wrapped function, such as its name, docstring, and annotations, making debugging and introspection more reliable.
    def wrapper(*args, **kwargs):
        start = perf_counter()

        try:
            return func(*args, **kwargs)

        finally:
            elapsed = perf_counter() - start
            print(elapsed)

    return wrapper

@measure_time
def process_chunks(chunks: list[str]) -> int:
    return sum(len(chunk) for chunk in chunks)

# A decorator adds behavior around a function. It does not necessarily change the underlying business logic.
