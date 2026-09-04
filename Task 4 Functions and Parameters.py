#Task 4 Functions and Parameters

def get_materials_database():
    """Creates and returns the materials database."""
    materials_db = {
        "Steel": {"yield_strength": 250.0, "youngs_modulus": 200.0},
        "Aluminum": {"yield_strength": 95.0, "youngs_modulus": 69.0},
        "Titanium": {"yield_strength": 880.0, "youngs_modulus": 114.0}
    }
    return materials_db


def get_material_properties(material_name, database):
    """Gets the properties of a material from the database."""
    db_lookup = {key.lower(): key for key in database}

    if material_name.lower() in db_lookup:
        material = db_lookup[material_name.lower()]
        return database[material]

    raise KeyError(f"Material '{material_name}' not found in database!")


def get_test_inputs():
    """Gets and validates the inputs needed for a calculation."""
    force = get_validated_input("Enter applied force (N): ", validate_positive_number)
    area = get_validated_input("Enter cross-sectional area (m²): ", validate_positive_number)
    original_length = get_validated_input("Enter original length (m): ", validate_positive_number)
    change_in_length = get_validated_input("Enter change in length (m): ", validate_non_zero)

    return {
        "force": force,
        "area": area,
        "original_length": original_length,
        "change_in_length": change_in_length
    }


def perform_calculation(material, inputs, database):
    """Performs all calculations for the selected material."""
    properties = get_material_properties(material, database)

    stress_pa = calculate_stress(inputs["force"], inputs["area"])
    stress_mpa = stress_pa / 1000000

    strain = calculate_strain(inputs["original_length"], inputs["change_in_length"])

    calc_modulus_pa = calculate_youngs_modulus(stress_pa, strain)
    calc_modulus_gpa = calc_modulus_pa / 100000000

    safety_factor = calculate_factor_of_safety(properties["yield_strength"], stress_pa)

    if stress_mpa >= properties["yield_strength"]:
        safety_status = "DANGER"
    elif safety_factor < 1.25:
        safety_status = "CAUTION"
    else:
        safety_status = "SAFE"

    return {
        "stress_pa": stress_pa,
        "stress_mpa": stress_mpa,
        "strain": strain,
        "calc_modulus_gpa": calc_modulus_gpa,
        "safety_factor": safety_factor,
        "safety_status": safety_status
    }