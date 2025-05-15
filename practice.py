def calculate_bmi(weight, height):
    
    height_m = height / 100  
    bmi = weight / (height_m ** 2)
    return bmi

def suggest_plan(bmi):
    """Suggest workout duration and basic diet plan based on BMI"""
    if bmi < 18.5:
        return "Underweight", "Workout Duration: 20 mins light exercise\nDiet Plan: High-protein and calorie-rich foods."
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight", "Workout Duration: 30-45 mins moderate exercise\nDiet Plan: Balanced diet with proteins, carbs, and vegetables."
    elif 25 <= bmi <= 29.9:
        return "Overweight", "Workout Duration: 45-60 mins cardio and strength\nDiet Plan: Low-carb diet with high fiber and lean protein."
    else:
        return "Obese", "Workout Duration: 60+ mins cardio-focused\nDiet Plan: Strict low-calorie, low-fat diet with professional guidance."

def get_user_input(checkcondition):
    """User input safely with validate and exception handling"""
    while True:
        try:
            value = input(checkcondition).strip()
            if not value:
                raise ValueError("Input cannot be empty.")
            value = float(value)
            if value <= 0:
                raise ValueError("Input must be a positive number.")
            return value
        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def workout_time_planner():
    print("Welcome to the Workout Time Planner!")
    
    weight = get_user_input("Enter your weight in kg: ")
    height = get_user_input("Enter your height in cm: ")
    
    try:
        bmi = calculate_bmi(weight, height)
        status, plan = suggest_plan(bmi)
        print(f"\nYour BMI is: {bmi:.2f} ({status})")
        print(plan)
    except Exception as e:
        print(f"An error occurred while calculating BMI or generating the plan: {e}")


workout_time_planner()
