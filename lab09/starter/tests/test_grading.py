"""Example tests to show the structure. Lab 9 asks for at least 15 test cases:
normal inputs, boundary values and error conditions. Add yours below.

Run from lab09/starter:
    pytest
    pytest --cov=gradebook --cov-report=term-missing --cov-report=html
"""

import pytest

from gradebook.grading import letter_grade, drop_lowest, grade_points, weighted_average, late_penalty


def test_letter_grade_normal_score_returns_b():
    assert letter_grade(85) == "B"

def test_letter_grade_above_100_raises_value_error():
    with pytest.raises(ValueError):
        letter_grade(100.5)

def test_letter_grade_bellow_0_raises_value_error():
    with pytest.raises(ValueError):
        letter_grade(-10)

def test_drop_lowest_returns_new_list():
    assert drop_lowest([90, 80, 70]) == [90, 80]

def test_drop_lowest_one_item_raises_error():
    with pytest.raises(ValueError):
        drop_lowest([90])

def test_drop_lowest_negative_number_raises_error():
    with pytest.raises(ValueError):
        drop_lowest([-100])

def test_grade_points_non_number_raises_type_error():
    with pytest.raises(TypeError):
        grade_points(420)

def test_grade_points_letter_raises_value_error():
    with pytest.raises(ValueError):
        grade_points("v")

def test_grade_point_B_returns_normal_score():
    grade_points("B") == 83

def test_weighted_average_empty_value_raises_value_error():
    with pytest.raises(ValueError):
        weighted_average({"labs": [90,80]}, {"labs": 0})

def test_weighted_average_negative_weight_raises_value_error():
    with pytest.raises(ValueError):
        weighted_average({"labs": [90,80], "exams": [70, 60]}, {"labs": -.8, "exams": 1.8})

def test_weighted_average_weights_add_above_1_raises_value_error():
    with pytest.raises(ValueError):
        weighted_average({"labs": [90, 80], "exams": [70, 60]}, {"labs": .7, "exams": 1})

def test_weighted_average_extra_category_raises_value_error():
    with pytest.raises(ValueError):
        weighted_average({"labs": [90, 80], "exams": [20]}, {"labs": 1.0})

def test_weighted_average_extra_weight_raises_value_error():
    with pytest.raises(ValueError):
        weighted_average({"labs": [90, 80]}, {"labs": .3, "exams": .7})

def test_weighted_average_returns_normal_weighted_average():
    assert weighted_average({"labs": [90, 80], "exams": [70, 60]}, {"labs": .3, "exams": .7}) == 71.0

def test_late_penalty_returns_normal_value():
    assert late_penalty(100, 2) == 80

def test_late_penalty_score_returns_value_error():
    with pytest.raises(ValueError):
        late_penalty(101, 1)

def test_late_penalty_score_returns_type_error():
    with pytest.raises(TypeError):
        late_penalty("not a score", 1)

def test_late_penalty_days_late_under_0():
    with pytest.raises(ValueError):
        late_penalty(100, -1)

def test_late_penalty_days_late_returns_type_error():
    with pytest.raises(TypeError):
        late_penalty(100, "Not a number")

# TODO: boundary values (exactly 93? 92.99? 0? 100?), drop_lowest, grade_points,
#       weighted_average, roster_loader, repository, service ...
