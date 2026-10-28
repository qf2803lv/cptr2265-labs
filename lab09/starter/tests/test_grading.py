"""Example tests to show the structure. Lab 9 asks for at least 15 test cases:
normal inputs, boundary values and error conditions. Add yours below.

Run from lab09/starter:
    pytest
    pytest --cov=gradebook --cov-report=term-missing --cov-report=html
"""

import pytest

from gradebook.grading import letter_grade


def test_letter_grade_normal_score_returns_b():
    assert letter_grade(85) == "B"


def test_letter_grade_above_100_raises_value_error():
    with pytest.raises(ValueError):
        letter_grade(100.5)


# TODO: boundary values (exactly 93? 92.99? 0? 100?), drop_lowest, grade_points,
#       weighted_average, roster_loader, repository, service ...
