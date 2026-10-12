"""
PYTHON BASICS SUMMARY
=====================

This file summarizes the topics covered:
1. Python data structures and mutability
2. Aliasing vs copying; mutable objects inside tuples
3. Basic coding exercises: reverse string, largest number, character frequency
4. Reading TXT files
5. Reading PDFs with pypdf
6. Reading CSV and Excel files with pandas
7. Getting CSV row/column counts and column names

INSTALL OPTIONAL LIBRARIES
--------------------------
For TXT and data-structure examples, Python's standard library is enough.

For PDFs:
    uv add pypdf
    # or: pip install pypdf

For CSV/Excel:
    uv add pandas openpyxl
    # or: pip install pandas openpyxl

Run:
    python python_basics_summary.py

File paths are examples. Update them to match your files before calling the
document-extraction functions.
"""

from pathlib import Path
import re
from typing import Any


# ============================================================================
# 1. PYTHON DATA STRUCTURES
# ============================================================================

def data_structure_examples() -> None:
    """Demonstrate common built-in data structures and their behavior."""

    # LIST: ordered, allows duplicates, mutable.
    numbers = [10, 20, 30, 20]
    numbers[0] = 100
    numbers.append(40)
    print("List (mutable):", numbers)

    # TUPLE: ordered, allows duplicates, immutable container.
    coordinates = (10, 20, 10)
    print("Tuple (immutable):", coordinates)
    # coordinates[0] = 99  # TypeError: tuple items cannot be reassigned.

    # SET: unique elements, mutable, no positional indexing.
    unique_numbers = {10, 20, 30, 20}
    unique_numbers.add(40)
    print("Set (unique values):", unique_numbers)

    # Set operations: union, intersection, difference.
    first = {1, 2, 3}
    second = {3, 4, 5}
    print("Union:", first | second)
    print("Intersection:", first & second)
    print("Difference:", first - second)

    # DICTIONARY: mutable key-value mapping; keys must be hashable.
    user = {"name": "Balaji", "age": 27, "city": "Chennai"}
    user["age"] = 28
    user["role"] = "AI Engineer"
    print("Dictionary:", user)
    print("Dictionary name:", user["name"])
    for key, value in user.items():
        print(f"  {key}: {value}")

    # STRING: ordered sequence of characters, but immutable.
    text = "hello"
    # text[0] = "H"  # TypeError: strings cannot be changed in place.
    text = "H" + text[1:]  # Creates a new string.
    print("String (immutable):", text)

    # RANGE: immutable sequence, often used for loops.
    print("Range:", list(range(2, 10, 2)))


def mutability_summary() -> dict[str, str]:
    """Return a quick mutability reference."""
    return {
        "list": "Mutable",
        "tuple": "Immutable container (but may contain mutable objects)",
        "set": "Mutable",
        "dict": "Mutable",
        "str": "Immutable",
        "range": "Immutable",
        "int / float / bool": "Immutable",
        "frozenset / bytes": "Immutable",
    }


# ============================================================================
# 2. ALIASING, COPYING, AND MUTABLE OBJECTS INSIDE TUPLES
# ============================================================================

def copy_examples() -> None:
    """Show why assigning a list to another variable does not copy it."""

    original = [1, 2, 3]
    alias = original
    alias.append(4)
    print("Aliasing - original:", original)  # [1, 2, 3, 4]
    print("Aliasing - alias:", alias)        # [1, 2, 3, 4]

    original = [1, 2, 3]
    separate_copy = original.copy()  # Shallow copy; separate outer list.
    separate_copy.append(4)
    print("Copied original:", original)       # [1, 2, 3]
    print("Separate copy:", separate_copy)   # [1, 2, 3, 4]

    # A tuple cannot have its elements reassigned, but a contained list can
    # still be changed because that list is a separate mutable object.
    mixed = ([1, 2, 3], 10)
    mixed[0].append(4)
    print("Tuple containing a list:", mixed)
    # mixed[0] = [5, 6]  # TypeError: cannot reassign a tuple element.


# ============================================================================
# 3. BASIC CODING QUESTIONS — WITH SOLUTIONS
# ============================================================================

def reverse_string(text: str) -> str:
    """Return a reversed string without using reversed() or slicing."""
    characters = []
    for character in text:
        characters.insert(0, character)
    return "".join(characters)


def reverse_string_two_pointers(text: str) -> str:
    """Alternative: reverse using a list and two pointers."""
    characters = list(text)
    left, right = 0, len(characters) - 1

    while left < right:
        characters[left], characters[right] = characters[right], characters[left]
        left += 1
        right -= 1

    return "".join(characters)


def find_largest(numbers: list[float]) -> float:
    """Find the largest number without using max(); reject an empty list."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


def char_frequency(text: str, ignore_spaces: bool = False) -> dict[str, int]:
    """
    Count character frequency.
    Set ignore_spaces=True to ignore whitespace and count case-insensitively.
    """
    if ignore_spaces:
        text = "".join(text.lower().split())

    counts: dict[str, int] = {}
    for character in text:
        counts[character] = counts.get(character, 0) + 1
    return counts


# ============================================================================
# 4. TXT FILE EXTRACTION
# ============================================================================

def read_txt(file_path: str | Path) -> str:
    """
    Read an entire text file as one string.
    encoding='utf-8' handles common text files; errors='replace' prevents
    decoding errors from stopping extraction when invalid bytes are present.
    """
    path = Path(file_path)
    return path.read_text(encoding="utf-8", errors="replace")


def read_txt_lines(file_path: str | Path) -> list[str]:
    """Read a text file line by line and remove surrounding whitespace."""
    with Path(file_path).open("r", encoding="utf-8", errors="replace") as file:
        return [line.strip() for line in file]


def parse_colon_separated_txt(file_path: str | Path) -> dict[str, str]:
    """
    Parse lines such as 'Name: Balaji' into a dictionary.
    Lines without ':' are skipped. split(':', 1) only splits at the first colon.
    """
    result: dict[str, str] = {}
    for line in read_txt_lines(file_path):
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


# ============================================================================
# 5. PDF EXTRACTION
# ============================================================================

def extract_pdf_pages(file_path: str | Path) -> list[dict[str, Any]]:
    """
    Extract text page by page using pypdf.
    Keeps page numbers so a later RAG system can cite the source page.

    Install: uv add pypdf
    Note: image-only/scanned PDFs usually need OCR; pypdf alone cannot read
    text that exists only inside an image.
    """
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise ImportError("Install pypdf first: uv add pypdf") from exc

    path = Path(file_path)
    reader = PdfReader(str(path))
    pages: list[dict[str, Any]] = []

    for page_number, page in enumerate(reader.pages, start=1):
        extracted = page.extract_text() or ""
        pages.append({
            "file_name": path.name,
            "page_number": page_number,
            "text": extracted.strip(),
            "source_type": "pdf",
        })

    return pages


def extract_pdf_all_text(file_path: str | Path) -> str:
    """Join non-empty page text into a single string."""
    pages = extract_pdf_pages(file_path)
    return "\n\n".join(page["text"] for page in pages if page["text"])


# ============================================================================
# 6. CSV EXTRACTION AND ROW/COLUMN COUNTS
# ============================================================================

def read_csv_dataframe(file_path: str | Path):
    """
    Read a CSV into a pandas DataFrame.
    A DataFrame is a table of rows and columns.

    Install: uv add pandas
    """
    try:
        import pandas as pd
    except ImportError as exc:
        raise ImportError("Install pandas first: uv add pandas") from exc

    return pd.read_csv(file_path)


def csv_shape(file_path: str | Path) -> tuple[int, int]:
    """
    Return (row_count, column_count).
    df.shape is (rows, columns). The header is not counted as a data row.
    """
    df = read_csv_dataframe(file_path)
    rows, columns = df.shape
    return int(rows), int(columns)


def csv_column_names(file_path: str | Path) -> list[str]:
    """Return CSV column names as a normal Python list."""
    df = read_csv_dataframe(file_path)
    return df.columns.tolist()


def csv_to_records(file_path: str | Path) -> list[dict[str, Any]]:
    """Convert CSV rows to a list of dictionaries, one dictionary per row."""
    df = read_csv_dataframe(file_path)
    return df.to_dict(orient="records")


def csv_rows_as_text(file_path: str | Path) -> list[dict[str, Any]]:
    """
    Convert structured CSV rows into meaningful text plus metadata.
    Useful as a starting point for RAG; adapt the text fields to your dataset.
    """
    df = read_csv_dataframe(file_path)
    path = Path(file_path)
    records: list[dict[str, Any]] = []

    for row_number, record in enumerate(df.to_dict(orient="records"), start=1):
        row_text = "\n".join(
            f"{column}: {value}"
            for column, value in record.items()
            if value is not None
        )
        records.append({
            "text": row_text,
            "metadata": {
                "file_name": path.name,
                "row_number": row_number,
                "source_type": "csv",
            },
        })

    return records


# ============================================================================
# 7. EXCEL EXTRACTION
# ============================================================================

def read_excel_sheets(file_path: str | Path) -> dict[str, Any]:
    """
    Read every sheet from an .xlsx file.
    Returns a dictionary: sheet name -> pandas DataFrame.

    Install: uv add pandas openpyxl
    """
    try:
        import pandas as pd
    except ImportError as exc:
        raise ImportError("Install pandas and openpyxl: uv add pandas openpyxl") from exc

    return pd.read_excel(file_path, sheet_name=None)


def excel_to_records(file_path: str | Path) -> dict[str, list[dict[str, Any]]]:
    """
    Convert each Excel sheet to records while preserving sheet names.
    """
    sheets = read_excel_sheets(file_path)
    return {
        sheet_name: dataframe.to_dict(orient="records")
        for sheet_name, dataframe in sheets.items()
    }


def excel_rows_as_text(file_path: str | Path) -> list[dict[str, Any]]:
    """
    Convert Excel rows into text and preserve workbook, sheet, and row metadata.
    This helps maintain traceability when retrieving information later.
    """
    path = Path(file_path)
    sheets = read_excel_sheets(file_path)
    result: list[dict[str, Any]] = []

    for sheet_name, dataframe in sheets.items():
        for row_number, record in enumerate(
            dataframe.to_dict(orient="records"), start=1
        ):
            row_text = "\n".join(
                f"{column}: {value}"
                for column, value in record.items()
                if value is not None
            )
            result.append({
                "text": row_text,
                "metadata": {
                    "file_name": path.name,
                    "sheet_name": sheet_name,
                    "row_number": row_number,
                    "source_type": "xlsx",
                },
            })

    return result


# ============================================================================
# 8. CLEANING EXTRACTED TEXT
# ============================================================================

def normalize_whitespace(text: str) -> str:
    """
    Collapse repeated whitespace into single spaces.
    Use carefully: do not flatten text if line breaks/table layout are meaningful.
    """
    return re.sub(r"\s+", " ", text).strip()


# ============================================================================
# 9. DEMONSTRATION
# ============================================================================

def main() -> None:
    print("=== Data structures ===")
    data_structure_examples()
    print("\n=== Mutability reference ===")
    for data_type, status in mutability_summary().items():
        print(f"{data_type}: {status}")

    print("\n=== Copying ===")
    copy_examples()

    print("\n=== Basic coding exercises ===")
    print("Reverse string:", reverse_string("hello"))
    print("Reverse with two pointers:", reverse_string_two_pointers("hello"))
    print("Largest number:", find_largest([10, 25, 7, 42, 18]))
    print("Character frequency:", char_frequency("hello"))
    print(
        "Case-insensitive frequency, ignoring spaces:",
        char_frequency("Hello World", ignore_spaces=True),
    )

    print("\n=== File extraction usage examples ===")
    print("TXT: read_txt('data.txt')")
    print("PDF: extract_pdf_pages('documents/sample.pdf')")
    print("CSV counts: csv_shape('data.csv')")
    print("CSV columns: csv_column_names('data.csv')")
    print("CSV rows as dictionaries: csv_to_records('data.csv')")
    print("Excel sheets: read_excel_sheets('data.xlsx')")
    print("Excel records: excel_to_records('data.xlsx')")

    print(
        "\nThe file-extraction examples above are shown but not executed, "
        "because the example files may not exist on your computer."
    )


if __name__ == "__main__":
    main()
