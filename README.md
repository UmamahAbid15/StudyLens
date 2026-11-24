# StudyLens 🔎

**A Python-based intelligent study notes search assistant.**

## About the Project

StudyLens is a beginner-friendly Python project designed to explore the foundations of information retrieval and AI.

It allows users to search through study notes, identify matching paragraphs, and rank results based on keyword frequency.

## Features

- Read and process text files.
- Extract individual paragraphs.
- Search using keywords.
- Case-insensitive search.
- Rank results using keyword frequency.
- Handle empty queries and missing files.
- Continuous interactive search.
- Automated tests using Python unittest.

## Technologies Used

- Python
- Python Lists and Tuples
- Functions and List Comprehensions
- String Processing
- Linear Search
- Exception Handling
- unittest

## Project Structure

```text
StudyLens/
├── data/
│   └── notes.txt
├── src/
│   └── main.py
├── tests/
│   └── test_search.py
├── README.md
└── .gitignore
```

## Getting Started

1. Clone this repository.
2. Create a virtual environment:

   `python -m venv .venv`

3. Activate it on Windows:

   `.venv\Scripts\Activate.ps1`

4. Run StudyLens:

   `python src/main.py`

## Run Tests

`python -m unittest discover -s tests -v`

## Current Limitations

- Search is based on exact substring matching.
- Ranking uses keyword frequency.
- The application does not yet understand semantic meaning.

## Future Improvements

- NLP preprocessing.
- TF-IDF-based search.
- Semantic search.
- Document question answering.

---

**Project Status:** Version 0.1 — Basic Keyword Search Engine

Built as part of my Python and AI learning journey.