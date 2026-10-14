Q1. What is an iterator, and how does it work?
Interview answer: An iterator is an object that allows us to access elements one at a time. It implements the __iter__() and __next__() methods. The iter() function obtains an iterator, and next() retrieves the next element. When no elements remain, it raises StopIteration.

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
```

What is a generator in Python?
Interview answer: A generator is a convenient way to create an iterator. It uses the yield keyword to return values one at a time while preserving its execution state between calls. Generators are memory-efficient because they do not need to store all generated results simultaneously.

```python
def generate_numbers():
    yield 10
    yield 20
    yield 30

for number in generate_numbers():
    print(number)
    ```
I would use generators when processing large datasets, streaming LLM responses, reading documents incrementally, or generating batches for embedding and ingestion pipelines. They reduce peak memory usage by processing data incrementally rather than loading everything into memory.

```python
def read_text(path):
    with open(path) as file:
        for line in file:
            yield line.strip()
```

What is a dataclass?
Interview answer: A dataclass is a Python feature that automatically generates common methods such as __init__(), __repr__(), and equality comparisons based on declared fields. It reduces boilerplate when creating classes that primarily store data.

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

user = User("Arun", 25)
print(user)
```
What is a Pydantic model?
Interview answer: Pydantic models use type annotations to validate and parse input data at runtime. They are especially useful for API request and response schemas, configuration validation, and structured LLM outputs.  
```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int = Field(gt=0)

user = User(name="Arun", age=25)
print(user.model_dump())
```

What is an event loop?
Interview answer: An event loop is the central mechanism used by Python's asyncio framework to schedule and execute asynchronous tasks. When a task awaits an operation that cannot complete immediately, such as network I/O, the task can suspend, allowing other ready tasks to run. This is useful for handling many concurrent I/O operations without creating a thread for every task.

xplain the Python object model.
Interview answer: Python treats virtually everything as an object, including integers, strings, functions, classes, and instances. Objects have an identity, a type, and a value. Their behavior is defined by their type and, where applicable, special methods such as __str__, __len__, and __iter__.

What are magic methods or dunder methods?
These are special methods surrounded by double underscores that allow objects to integrate with Python language operations.
Examples:
- __init__() — initialize an instance.
- __str__() — define its human-readable string representation.
- __len__() — support len(obj).
- __iter__() and __next__() — support iteration.
- __eq__() — customize equality comparisons.

7. How does Python manage objects in memory?
Q1. Explain Python memory management.
Interview answer: Python manages object allocation and reclamation automatically. In CPython, memory management primarily uses reference counting, supported by a cyclic garbage collector that detects unreachable reference cycles. Python also uses internal allocators to manage memory efficiently.
Q2. What is reference counting?
Each object in CPython tracks references to it. When its reference count reaches zero, the object can generally be deallocated immediately.
getrefcount() itself temporarily adds a reference, so the result is usually one higher than the references held elsewhere.
```python
import sys

items = []
print(sys.getrefcount(items))
```
What is garbage collection?
Garbage collection helps reclaim objects involved in reference cycles that reference counting alone cannot free.

Q1. What is the purpose of __slots__?
Interview answer: __slots__ declares a fixed set of instance attributes for a class. In classes that would otherwise have an instance __dict__, using slots can reduce per-instance memory overhead and prevent arbitrary new attributes from being assigned.
This raises AttributeError in this example because city is not in __slots__ and there is no instance dictionary.
```python
class User:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Arun", 25)
print(user.name)
```
Explain shallow copy and deep copy.
Interview answer: A shallow copy creates a new outer object but keeps references to the original nested objects. A deep copy recursively copies nested objects, subject to the copying behavior of individual objects.

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99

print(shallow)  # [[99, 2], [3, 4]]
print(deep)     # [[1, 2], [3, 4]]
```
Why do we need locks in Python?
Interview answer: A lock coordinates access to shared mutable state between threads. Without synchronization, concurrent operations can interleave and produce inconsistent results. The Global Interpreter Lock (GIL) in standard CPython is not a substitute for application-level synchronization.
Q2. What is the difference between Lock and RLock?
Lock	RLock
Basic mutual-exclusion lock	Reentrant lock
Same thread cannot acquire it again while holding it without risking a deadlock	Same thread can acquire it repeatedly
One release unlocks a successful acquisition	Must be released the same number of times it was acquired

What is MRO in Python?
Interview answer: Method Resolution Order determines the sequence in which Python searches classes for an attribute or method, particularly when multiple inheritance is involved. Python uses the C3 linearization algorithm to produce a consistent order.
super() delegates method lookup to the next class in the MRO. It does not simply mean “call my direct parent.”

Why should a decorator use functools.wraps?
It preserves the original function's metadata, including its name, docstring, and annotations. This helps debugging, logging, and introspection.

How do you identify a performance bottleneck in Python?
Interview answer: I first measure the application under representative workloads. I use cProfile to identify functions consuming CPU time, time.perf_counter() for targeted timing, and tools such as tracemalloc to investigate Python memory allocations. Then I optimize the actual bottleneck and benchmark again.

Q12. How would you optimize searching across one million records?
Interview answer: I would choose the data structure based on the query pattern. For repeated exact-match lookups, I would use a dictionary or hash-based index keyed by a unique identifier. For database-backed data, I would use an appropriate database index rather than loading all records into memory. For range queries, sorting, binary search, or database indexes may be more suitable.

Q14. How can you optimize Python code processing large datasets?
- Avoid repeated database queries inside loops.
- Use dictionaries or sets for repeated membership checks.
- Process data in batches.
- Use vectorized operations in NumPy or pandas where appropriate.
- Cache expensive computations when inputs repeat and cache invalidation is manageable.
- Profile before rewriting code or adding concurrency.
Q15. What is caching, and when would you use lru_cache?
Caching stores the results of earlier computations so repeated calls can avoid recomputation.

```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def calculate_score(value):
    return value * value

print(calculate_score(10))
print(calculate_score(10))
print(calculate_score.cache_info())
``` 

Is Python interpreted or compiled?
Interview answer: Python is commonly described as an interpreted language, but CPython first compiles source code into bytecode. The Python virtual machine executes that bytecode. Unlike traditional ahead-of-time compilation to native machine code, this process usually happens at runtime.

. What is LEGB in Python?
LEGB describes the order used to resolve ordinary names:
- L — Local: Inside the current function.
- E — Enclosing: In enclosing function scopes.
- G — Global: At the module level.
- B — Built-in: Names such as len and sum.

What is a closure?
A closure is a function that retains access to variables from its enclosing scope even after the enclosing function has returned.

List are unhashable because they are mutable

Caching
1. In-memory caching
Fastest for local access
Stores data in the Python process's memory using dictionaries or functools.lru_cache.
Use case: Frequently called functions and configuration data.
2. Distributed caching
Uses Redis or Memcached to share cached data across multiple application instances.
Use case: FastAPI applications running on multiple servers.
3. TTL-based caching
Cached data expires automatically after a specified duration.
Use case: Stock prices, API responses, and frequently updated data.
4. Cache-aside (lazy loading)
The application checks the cache first. On a miss, it fetches from the database, returns the result, and populates the cache.
Use case: User profiles, product details, and database lookups.
5. Write-through caching
The application writes data to the cache and the backing database as part of the same logical write operation.
Use case: Systems where read performance and cache consistency are important.
6. HTTP / CDN caching
Caches HTTP responses in browsers, proxies, or CDNs using headers such as Cache-Control and ETag.
Use case: Static assets and cacheable GET endpoints.

Databse query cycle
What happens inside the database?
When Python sends a SQL query, a typical relational database follows these stages:
1. Connection establishment: The application connects using a driver such as mysql-connector-python, psycopg, or SQLAlchemy.
2. Parsing: The database checks SQL syntax and resolves table and column names.
3. Query planning and optimization: The optimizer chooses an execution plan, potentially using indexes and join strategies.
4. Execution: The database engine accesses the required data and performs filtering, joining, sorting, or aggregation.
5. Result retrieval: The result rows are sent back to the application.
6. Transaction completion: For write operations, the application commits or rolls back the transaction as appropriate

Why do we need a message broker?
Imagine a FastAPI application that receives a request to process 10,000 documents for a RAG application.
Without a message broker, the API might process all documents before returning a response. This can cause long response times and timeouts.
With a message broker, the API publishes a message, and a background worker processes the documents independently.

The typical message lifecycle is:
1. Producer: Creates and sends a message.
2. Broker: Accepts, stores, and routes the message.
3. Queue or topic: Holds messages for delivery or distributes them to subscribers.
4. Consumer: Receives and processes a message.
5. Acknowledgment (ACK): Confirms successful processing so the broker can mark the message as handled.
6. Retry or dead-letter queue (DLQ): Handles messages that repeatedly fail, according to the broker's configuration.
Common brokers, Rabbitmq, kafka, amazon sqs, redis