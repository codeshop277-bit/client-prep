numbers = [10,20,20]

iterator = iter(numbers)
print(next(iterator))
print(next(iterator))

squares = (x *x for x in range(5))
print(next(squares))
print(next(squares))

# Feature	List	Tuple	    Set         	      Dictionary
# Syntax	[]	    ()	        {1, 2}	              {"a": 1}
# Ordered	Yes	    Yes	        No guaranteed order	    Yes (insertion order)
# Mutable	Yes	    No	        Yes                 	Yes
# Duplicates	Allowed	Allowed	   Not allowed	        Keys must be unique
# Access	Index	Index	    Membership / iteration	   Key
# Common use	Modifiable collection	Fixed collection	Unique values	Key-value mapping

# 1. List: ordered and mutable
languages = ["Python", "Java", "Python"]
languages.append("JavaScript")

# 2. Tuple: ordered and immutable
coordinates = (10, 20, 30)

# 3. Set: unique elements
unique_languages = {"Python", "Java", "Python"}
unique_languages.add("JavaScript")

# 4. Dictionary: key-value pairs
developer = {
    "name": "John",
    "experience": 5,
    "skills": ["Python", "FastAPI"]
}

print("List:", languages)
print("Tuple:", coordinates)
print("Set:", unique_languages)
print("Dictionary:", developer)

languages = ["Python", "Java", "JavaScript"]

# Iterate over values
for language in languages:
    print(language)

# Iterate using indexes
for i in range(len(languages)):
    print(i, languages[i])

# Iterate in reverse
for language in reversed(languages):
    print(language)

# Iterate with index and value
for index, language in enumerate(languages):
    print(index, language)

skills = {"Python", "FastAPI", "LangChain"}

#Tuple Iteration
coordinates = (10, 20, 30)

for value in coordinates:
    print(value)

# Reverse iteration
for value in reversed(coordinates):
    print(value)

# Set Iteration
# Iterate over elements
for skill in skills:
    print(skill)

# Check membership
if "Python" in skills:
    print("Python is available")

#Dict
developer = {
    "name": "John",
    "experience": 5,
    "role": "AI Engineer"
}

# Iterate over keys
for key in developer:
    print(key)

# Iterate over values
for value in developer.values():
    print(value)

# Iterate over key-value pairs
for key, value in developer.items():
    print(key, value)