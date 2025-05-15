import pytest 

# Import the functions (assuming your main file is named 'workout_planner.py')
from practice import calculate_bmi, suggest_plan

# --- Unit Tests for calculate_bmi function ---
def test_calculate_bmi_normal_values():
    assert round(calculate_bmi(70, 170), 2) == 24.22  # Normal weight range

def test_calculate_bmi_underweight():
    assert round(calculate_bmi(45, 170), 2) == 15.57  # Underweight

def test_calculate_bmi_obese():
    assert round(calculate_bmi(100, 160), 2) == 39.06  # Obese

# --- Unit Tests for suggest_plan function ---
def test_suggest_plan_underweight():
    status, plan = suggest_plan(15.5)
    assert status == "Underweight"
    assert "20 mins light exercise" in plan

def test_suggest_plan_normal():
    status, plan = suggest_plan(23)
    assert status == "Normal weight"
    assert "30-45 mins moderate exercise" in plan

def test_suggest_plan_overweight():
    status, plan = suggest_plan(27)
    assert status == "Overweight"
    assert "45-60 mins cardio" in plan

def test_suggest_plan_obese():
    status, plan = suggest_plan(32)
    assert status == "Obese"
    assert "60+ mins cardio" in plan
