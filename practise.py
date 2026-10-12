from pathlib import Path

with Path("data.txt").open("r") as file:
    data = file.read()
    print([line.strip() for line in data.splitlines()])