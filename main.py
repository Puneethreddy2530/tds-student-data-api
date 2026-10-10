from pathlib import Path
import csv

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TDS Student Data API")

# Allow browser-based graders to call this public GET API from any origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

CSV_PATH = Path(__file__).with_name("students.csv")


def read_students() -> list[dict]:
    """Load the CSV once, preserving its original row order."""
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None or not {"studentId", "class"}.issubset(reader.fieldnames):
            raise RuntimeError("students.csv must contain studentId and class columns")

        return [
            {"studentId": int(row["studentId"]), "class": row["class"]}
            for row in reader
        ]


STUDENTS = read_students()


@app.get("/")
def root() -> dict:
    return {"message": "TDS Student Data API", "endpoint": "/api"}


@app.get("/api")
def get_students(class_: list[str] | None = Query(default=None, alias="class")) -> dict:
    """Return all students, or those belonging to any requested class values."""
    if not class_:
        selected = STUDENTS
    else:
        requested_classes = set(class_)
        # Filtering the source list preserves CSV row order, not query parameter order.
        selected = [student for student in STUDENTS if student["class"] in requested_classes]

    return {"students": selected}
