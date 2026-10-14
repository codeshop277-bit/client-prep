#The normalize_embeddings=True option normalizes the vectors to unit length. This is useful when you want to use dot product as cosine similarity.
#Cosine similarity measures the angle between two vectors:

from functools import wraps
import time
from fastapi import HTTPException

def retry_on_conn_errror(max=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0

            while True:
                try:
                    return func(*args, **kwargs)

                except ConnectionError:
                    retries+=1

                    if retries >= max:
                        raise HTTPException(
                            detail="maxed out"
                        )
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_on_conn_errror(max=3, delay=1)
def fetch_user():
    print("Connecting to database...")
    raise ConnectionError("Database connection failed")


try:
    fetch_user()
except ConnectionError as e:
    print(f"Final error: {e}")