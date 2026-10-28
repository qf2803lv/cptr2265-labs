import pytest

from gradebook.roster_loader import load_roster

def test_value_error_from_missing_category():
    with pytest.raises(ValueError):
        load_roster("data/test_roster1.csv")

def test_value_error_from_incorrect_type_for_score():
    with pytest.raises(ValueError):
        load_roster("data/test_roster2.csv")

def test_value_error_from_missing_value():
    with pytest.raises(ValueError):
        load_roster("data/test_roster3.csv")

def test_load_roster_returns_normal_value():
    assert load_roster("data/test_roster4.csv") == [{"student_id": "S001", "name": "Bob", "category": "labs", "score": 80}]