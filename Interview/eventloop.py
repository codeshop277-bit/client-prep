
import asyncio
import httpx


async def fetch_users(client: httpx.AsyncClient) -> list[dict]:
    print("A: Sending API request")

    response = await client.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    response.raise_for_status()
    print("C: API response received")

    return response.json()


def process_users(users: list[dict]) -> list[dict]:
    print("D: Processing users")

    return [
        {
            "id": user["id"],
            "name": user["name"].upper(),
            "email": user["email"],
        }
        for user in users
    ]


async def get_customer_report() -> list[dict]:
    print("1: Parent started")

    async with httpx.AsyncClient(timeout=10.0) as client:
        users = await fetch_users(client)

        processed_users = process_users(users)

        print(f"E: Processed {len(processed_users)} users")
        return processed_users


async def main():
    report = await get_customer_report()
    print("F: Parent received report:", len(report))


if __name__ == "__main__":
    asyncio.run(main())


# asyncio.run(main())
# Python creates and runs an event loop and starts the main() coroutine as a task.

# Parent calls the child
# get_customer_report() calls fetch_users() and awaits it. Both coroutines execute in the same task here; creating a separate task is not necessary.

# Request starts
# await client.get(...) initiates the HTTP operation. Once the HTTP client reaches an asynchronous I/O wait, the coroutine suspends and gives control back to the event loop.

# Network wait
# The operating system and network handle the connection, request transmission, and response arrival. The event loop monitors I/O readiness. Other ready tasks and callbacks can run during this period.

# Response becomes ready
# The HTTP client's internal I/O handling processes incoming data. When the awaited operation completes, the waiting task is made ready to resume.

# Response processing
# Execution continues after await client.get(...). The code parses JSON, transforms the users, calculates the result, and returns to the parent.

# I/O readiness callback: Notifies the event loop that a socket can make progress, such as reading available bytes.
# Protocol/client handling: The HTTP library interprets the bytes, manages the HTTP response, and determines when the request completes. Some of this handling is callback-driven; exact internals depend on the client and event-loop implementation.
# Task wake-up callback: Once the awaited operation completes, asyncio schedules the suspended task to resume. Internally, task stepping advances the coroutine from the await point.