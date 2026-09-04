# Task 4: Functions And Parameters

def validate_positive_number(value, parameter_name):
    """Checks if a value is a positive number greater than zero."""
    if value <= 0:
        raise ValueError(f"{parameter_name} must be greater than zero.")
    return value


def validate_non_zero(value, parameter_name):
    """Checks if a value is not zero."""
    if value == 0:
        raise ValueError(f"{parameter_name} cannot be zero.")
    return value


def get_validated_input(prompt, validator_func):
    """Gets a number from the user and validates it."""
    while True:
        try:
            value = float(input(prompt))
            return validator_func(value, prompt)
        except ValueError as error:
            print(f"{error}. Please enter a valid number.")


def calculate_stress(force, area):
    """Calculates stress from force and cross-sectional area."""
    stress = force / area
    return stress


def calculate_strain(original_length, change_in_length):
    """Calculates strain from original length and change in length."""
    strain = change_in_length / original_length
    return strain


def calculate_youngs_modulus(stress, strain):
    """Calculates Young's modulus from stress and strain."""
    if strain == 0:
        return 0.0
    modulus = stress / strain
    return modulus


def calculate_factor_of_safety(yield_strength, stress):
    """Calculates the factor of safety using yield strength and stress."""
    if stress == 0:
        return 0.0
    safety = yield_strength / stress
    return safety