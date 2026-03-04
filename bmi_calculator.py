import tabulate
import csv

# --- NEW: Validation + Exceptions (Feature: Punkt 2) ---

class BMIInputError(ValueError):
    """Base exception for BMI input validation errors."""

class InvalidHeightError(BMIInputError):
    """Raised when height is missing or out of valid range."""

class InvalidWeightError(BMIInputError):
    """Raised when weight is missing or out of valid range."""

def validate_inputs(height: float, weight: float) -> None:
    """
    Validate height and weight with reasonable bounds.
    Raises:
        InvalidHeightError / InvalidWeightError
    """
    if height is None:
        raise InvalidHeightError("Height is required.")
    if weight is None:
        raise InvalidWeightError("Weight is required.")

    # Basic plausibility checks (in meters / kg, as your prompts indicate)
    if height <= 0:
        raise InvalidHeightError("Height must be greater than 0 meters.")
    if not (0.5 <= height <= 2.5):
        raise InvalidHeightError("Height must be between 0.50 m and 2.50 m.")

    if weight <= 0:
        raise InvalidWeightError("Weight must be greater than 0 kilograms.")
    if not (2 <= weight <= 400):
        raise InvalidWeightError("Weight must be between 2 kg and 400 kg.")

def reference_chart():
    """
    This is a function used to tabulate the data
    of the bmi scale for the user, this requries a csv file 'bmi.csv' and two libraries "csv" and "tabulate".
    It won't take any arguments and won't return anything
    """
    list2 = []
    with open("bmi.csv") as file1:
        list1 = csv.reader(file1)
        for line in list1:
            list2.append(line)
        print("Here You can take the reference chart \n")
        print(tabulate.tabulate(list2[1:], headers=list2[0], tablefmt="fancy_grid"))


def calculate_bmi(height, weight):
    """
    Calculate BMI given height (in meters) and weight (in kilograms).

    Args:
        height (float): Height in meters.
        weight (float): Weight in kilograms.

    Returns:
        float: Calculated BMI.
    """
    try:
        bmi = round(weight / (height**2), 2)
        return bmi
    except ZeroDivisionError:
        return None


def interpret_bmi(bmi):
    """
    Interpret the BMI and provide a classification.

    Args:
        bmi (float): Calculated BMI.

    Returns:
        str: BMI interpretation.
    """
    if bmi is None:
        return "Invalid input. Height should be greater than 0."

    if bmi < 18.5:
        return f"Your BMI is {bmi}, you are underweight."
    elif bmi < 24.9:
        return f"Your BMI is {bmi}, you have a normal weight."
    elif bmi < 29.9:
        return f"Your BMI is {bmi}, you are overweight."
    elif bmi < 34.9:
        return f"Your BMI is {bmi}, you are obese (Class I)."
    elif bmi < 39.9:
        return f"Your BMI is {bmi}, you are obese (Class II)."
    else:
        return f"Your BMI is {bmi}, you are obese (Class III)."


def main():
    reference_chart()
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))

        bmi = calculate_bmi(height, weight)
        result = interpret_bmi(bmi)
        print(result)

    except ValueError:
        print("Invalid input. Please enter numerical values for height and weight.")


if __name__ == "__main__":
    main()