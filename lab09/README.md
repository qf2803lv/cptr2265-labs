# Lab 9 Starter: Gradebook Module (Python)

Requires **Python 3.10+**. Use this starter for Lab 9 if you are not testing a module from your midterm project. It is designed to carry into **Lab 10** as well: it already has a file-system dependency to mock and a database to use in integration tests.

Unzip this into the root of your `cptr2265-labs` repository so the files land in `lab09/starter/`.

## What's inside
| Path | What it is | Good for |
|---|---|---|
| `gradebook/grading.py` | Pure grading rules: `letter_grade`, `grade_points`, `drop_lowest`, `weighted_average` | Lab 9 Part A unit tests (normal, boundary, error cases) |
| `gradebook/roster_loader.py` | `load_roster(path)` reads a CSV from disk | Lab 10 Part A: mock the file system |
| `gradebook/repository.py` | `StudentRepository` stores students and scores in SQLite | Lab 10 Part B: integration tests with `sqlite3.connect(":memory:")` |
| `gradebook/service.py` | `GradebookService` ties the pieces together; dependencies are passed into the constructor | Mocking and integration tests |
| `gradebook/__main__.py` | A small demo that prints a class report | Seeing it run |
| `data/sample_roster.csv` | Sample data for the demo and for tests | |
| `tests/test_grading.py` | Two example tests to show the structure | Add your tests here (and in new `tests/test_*.py` files) |

## Setup and run
```
cd lab09/starter
python -m venv .venv
.venv\Scripts\activate          # Windows   (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt

python -m gradebook             # run the demo
pytest                          # run the tests
pytest --cov=gradebook --cov-report=term-missing --cov-report=html   # coverage (Part C)
```
The HTML coverage report is written to `htmlcov/index.html`. The demo file (`__main__.py`) is excluded from coverage in `.coveragerc`.

## Part B ideas (strict TDD)
Write the test first and commit it failing, make it pass and commit, then refactor and commit. Pick one of these new functions for `grading.py` (or propose your own):
- `class_statistics(percentages)` returns mean, median, minimum and maximum; decide what happens with an empty list.
- `curve(scores, target_mean)` shifts every score so the average equals `target_mean`, capping at 100.
- `gpa(letter_grades, credits)` computes a credit-weighted GPA using `grade_points`.
- `late_penalty(score, days_late)` subtracts 10% per day late, with 0 at 5 or more days.

## Looking ahead to Lab 10
- **Mocking:** `GradebookService(repo, loader=fake_loader)` accepts any loader, so a `unittest.mock.Mock` can stand in for the file system. You can also use `unittest.mock.patch("builtins.open", ...)` when testing `load_roster` directly.
- **Integration tests:** build a real `StudentRepository(sqlite3.connect(":memory:"))` in a pytest fixture, import `data/sample_roster.csv` through the service, and check the class report.
