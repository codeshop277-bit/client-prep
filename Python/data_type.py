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