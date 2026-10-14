from pydantic import BaseModel, EmailStr, Field
from fastapi import Fastapi, HTTPException, status
from tenacity import (retry, retry_if_exception_type, stop_after_attempt, wait_exponential)

class UserCreate:
    name: str
    email: EmailStr
    age: int

class UserResponse:
    id: int
    name:str
    email: EmailStr
    age: int

app = Fastapi(title="User API")

@retry(
    retry = retry_if_exception_type(ConnectionError),
    stop = stop_after_attempt(3),
    wait = wait_exponential(multiplier=1, min=1, max=4),
    reraise=True # helps in catchin original exception else it throws RetryExhaust
)
async def create_user(data) -> dict:
    return "test+"

@app.post("/users", response_model=UserResponse)
async def create_users(data: UserCreate):
    try:
        result = await create_user(data)

    except ConnectionError:
        raise HTTPException(
            status_code=503,
            detail="Service unavailable"
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )