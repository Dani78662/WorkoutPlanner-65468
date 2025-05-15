def get_valid_input(prompt, data_type=float):
    while True:
        try:
            value = input(prompt)
            if value.strip() == "":
                raise ValueError("Input cannot be empty.")
            value = data_type(value)
            if value <= 0:
                raise ValueError("Value must be greater than zero.")
            return value
        except ValueError as e:
            print("Invalid input:", e)

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return weight / (height_m ** 2)

def suggest_plan(bmi):
    if bmi < 18.5:
        return "30 mins light workout, high-protein diet", "Home"
    elif bmi < 25:
        return "45 mins moderate workout, balanced diet", "Home"
    elif bmi < 30:
        return "60 mins workout, low-carb diet", "Gym"
    else:
        return "90 mins workout, strict low-fat diet", "Gym"

def main():
    print("Welcome to the Workout Time Planner")
    weight = get_valid_input("Enter your weight in kg: ")
    height = get_valid_input("Enter your height in cm: ")

    bmi = calculate_bmi(weight, height)
    plan, location = suggest_plan(bmi)

    print(f"\nYour BMI is {bmi:.2f}")
    print("Suggested Workout Plan:", plan)
    print("Recommended Location:", location)

if __name__ == "__main__":
    main()
