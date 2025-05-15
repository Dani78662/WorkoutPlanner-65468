from workout_planner import calculate_bmi, suggest_plan

def test_bmi_calculation():
    assert round(calculate_bmi(70, 175), 2) == 22.86
    assert round(calculate_bmi(50, 160), 2) == 19.53

def test_suggest_plan_underweight():
    plan, location = suggest_plan(17.0)
    assert "light workout" in plan.lower()
    assert location == "Home"

def test_suggest_plan_normal():
    plan, location = suggest_plan(23.0)
    assert "balanced" in plan.lower()
    assert location == "Home"

def test_suggest_plan_overweight():
    plan, location = suggest_plan(27.0)
    assert "low-carb" in plan.lower()
    assert location == "Gym"

def test_suggest_plan_obese():
    plan, location = suggest_plan(35.0)
    assert "strict" in plan.lower()
    assert location == "Gym"
