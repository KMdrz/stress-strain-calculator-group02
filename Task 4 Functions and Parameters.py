# Task 4: Functions and Parameters

def validate_positive_number(
    value: float,
    parameter_name: str
) -> float:
    """Validate that a number is greater than zero."""
    if value <= 0:
        raise ValueError(
            f"{parameter_name} must be greater than zero."
        )
    return value


def validate_non_zero(
    value: float,
    parameter_name: str
) -> float:
    """Validate that a number is not zero."""
    if value == 0:
        raise ValueError(
            f"{parameter_name} cannot be zero."
        )
    return value


def validate_force(
    value: float,
    parameter_name: str
) -> float:
    """Validate force while allowing negative compression values."""
    if value == 0:
        raise ValueError(
            f"{parameter_name} cannot be zero."
        )
    return value


def get_validated_input(
    prompt: str,
    validator_func
) -> float:
    """Get numeric input and validate it."""
    while True:
        try:
            value = float(input(prompt))
            return validator_func(value, prompt)
        except ValueError as error:
            print(f"  [Error]: {error}")


def calculate_stress(
    force: float,
    area: float
) -> float:
    """Calculate stress from force and cross-sectional area."""
    return force / area


def calculate_strain(
    original_length: float,
    change_in_length: float
) -> float:
    """Calculate strain from length measurements."""
    return change_in_length / original_length


def calculate_youngs_modulus(
    stress: float,
    strain: float
) -> float:
    """Calculate Young's modulus from stress and strain."""
    if strain == 0:
        return 0.0
    return stress / strain


def calculate_factor_of_safety(
    yield_strength: float,
    stress: float
) -> float:
    """Calculate factor of safety using absolute stress."""
    if stress == 0:
        return float("inf")
    return yield_strength / abs(stress)


def get_materials_database() -> dict:
    """Return the built-in materials database."""
    return {
        "Steel": {
            "yield_strength": 250.0,
            "youngs_modulus": 200.0
        },
        "Aluminum": {
            "yield_strength": 95.0,
            "youngs_modulus": 69.0
        },
        "Titanium": {
            "yield_strength": 880.0,
            "youngs_modulus": 114.0
        }
    }


def get_material_properties(
    material_name: str,
    database: dict
) -> dict:
    """Return properties for a material by name."""
    db_lookup = {
        key.lower(): key
        for key in database
    }

    name = material_name.strip().lower()

    if name in db_lookup:
        return database[db_lookup[name]]

    raise KeyError(
        f"Material '{material_name}' not found in database!"
    )


def get_test_inputs() -> dict:
    """Get and validate inputs for one calculation."""
    force = get_validated_input(
        "Enter applied force (N): ",
        validate_force
    )

    area = get_validated_input(
        "Enter cross-sectional area (m²): ",
        validate_positive_number
    )

    original_length = get_validated_input(
        "Enter original length (m): ",
        validate_positive_number
    )

    change_in_length = get_validated_input(
        "Enter change in length (m): ",
        validate_positive_number
    )

    return {
        "force": force,
        "area": area,
        "original_length": original_length,
        "change_in_length": change_in_length
    }


def perform_calculation(
    material: str,
    inputs: dict,
    database: dict
) -> dict:
    """Perform calculations and return the results."""
    properties = get_material_properties(
        material,
        database
    )

    stress_pa = calculate_stress(
        inputs["force"],
        inputs["area"]
    )

    strain = calculate_strain(
        inputs["original_length"],
        inputs["change_in_length"]
    )

    stress_mpa = stress_pa / 1_000_000

    modulus_pa = calculate_youngs_modulus(
        stress_pa,
        strain
    )

    modulus_gpa = modulus_pa / 1_000_000_000

    safety_factor = calculate_factor_of_safety(
        properties["yield_strength"],
        stress_mpa
    )

    if abs(stress_mpa) >= properties["yield_strength"]:
        safety_status = "DANGER"
    elif safety_factor < 1.25:
        safety_status = "CAUTION"
    else:
        safety_status = "SAFE"

    loading = (
        "Tension"
        if stress_mpa > 0
        else "Compression"
    )

    return {
        "stress_pa": stress_pa,
        "stress_mpa": stress_mpa,
        "strain": strain,
        "calc_modulus_gpa": modulus_gpa,
        "safety_factor": safety_factor,
        "safety_status": safety_status,
        "loading": loading
    }


def create_calculation_record(
    material: str,
    inputs: dict,
    results: dict
) -> dict:
    """Create a complete calculation record."""
    return {
        "material": material,
        "force": inputs["force"],
        "area": inputs["area"],
        "original_length": inputs["original_length"],
        "change_in_length": inputs["change_in_length"],
        "stress_pa": results["stress_pa"],
        "stress_mpa": results["stress_mpa"],
        "strain": results["strain"],
        "calc_modulus_gpa": results["calc_modulus_gpa"],
        "safety_factor": results["safety_factor"],
        "safety_status": results["safety_status"],
        "loading": results["loading"]
    }


def add_to_history(
    history_list: list,
    record: dict
) -> None:
    """Add a calculation record to session history."""
    history_list.append(record)


def display_material_menu(database: dict) -> None:
    """Display all available materials."""
    print("\nAvailable Materials:")

    for material, properties in database.items():
        print(
            f"- {material} "
            f"(Yield: {properties['yield_strength']} MPa, "
            f"E: {properties['youngs_modulus']} GPa)"
        )

    print("- Custom")


def display_safety_analysis(
    stress: float,
    yield_strength: float,
    safety_factor: float
) -> None:
    """Display the safety analysis for a calculation."""
    print("\n===== SAFETY ANALYSIS =====")
    print(f"Applied Stress: {stress:.2f} MPa")
    print(f"Yield Strength: {yield_strength:.2f} MPa")
    print(f"Factor of Safety: {safety_factor:.2f}")


def display_calculation_results(
    record: dict,
    database: dict
) -> None:
    """Display the results of one calculation."""
    properties = database[record["material"]]

    print("\n===== CALCULATION RESULTS =====")
    print(f"Material: {record['material']}")
    print(f"Force: {record['force']} N")
    print(f"Area: {record['area']} m²")
    print(f"Original Length: {record['original_length']} m")
    print(f"Change in Length: {record['change_in_length']} m")
    print(f"Stress: {record['stress_mpa']:.2f} MPa")
    print(f"Strain: {record['strain']:.6f}")
    print(
        f"Young's Modulus: "
        f"{record['calc_modulus_gpa']:.2f} GPa"
    )
    print(f"Loading: {record['loading']}")
    print(
        f"Factor of Safety: "
        f"{record['safety_factor']:.2f}"
    )
    print(f"Safety Status: {record['safety_status']}")

    display_safety_analysis(
        record["stress_mpa"],
        properties["yield_strength"],
        record["safety_factor"]
    )


def display_session_summary(
    history: list,
    unique_materials: set
) -> None:
    """Display the complete session summary."""
    print("\n===== SESSION SUMMARY =====")
    print(f"Total Calculations: {len(history)}")
    print(f"Unique Materials: {len(unique_materials)}")

    if not history:
        print("No calculations performed.")
        return

    highest_stress = max(
        history,
        key=lambda x: abs(x["stress_mpa"])
    )

    lowest_safety = min(
        history,
        key=lambda x: x["safety_factor"]
    )

    average_strain = (
        sum(record["strain"] for record in history)
        / len(history)
    )

    failed_tests = [
        record for record in history
        if record["safety_status"] == "DANGER"
    ]

    valid_ratios = [
        record for record in history
        if record["strain"] != 0
    ]

    print("\n--- Statistical Analysis ---")
    print(
        f"Highest Stress: "
        f"{highest_stress['stress_mpa']:.2f} MPa "
        f"({highest_stress['material']})"
    )

    print(
        f"Lowest Factor of Safety: "
        f"{lowest_safety['safety_factor']:.2f} "
        f"({lowest_safety['material']})"
    )

    print(
        f"Average Strain: "
        f"{average_strain:.6f}"
    )

    if valid_ratios:
        best_ratio = min(
            valid_ratios,
            key=lambda x:
                abs(x["stress_mpa"]) / x["strain"]
        )

        ratio = (
            abs(best_ratio["stress_mpa"])
            / best_ratio["strain"]
        )

        print(
            f"Best Stress-to-Strain Ratio: "
            f"{ratio:.2f} "
            f"({best_ratio['material']})"
        )

    print("\n--- Failed Safety Checks ---")

    if failed_tests:
        for record in failed_tests:
            print(
                f"- {record['material']} "
                f"(Stress: {record['stress_mpa']:.2f} MPa)"
            )
    else:
        print("None")


def setup_program() -> tuple:
    """Initialize the database and session data."""
    database = get_materials_database()
    history = []
    unique_materials = set()

    return database, history, unique_materials


def handle_material(database: dict) -> str:
    """Get an existing or custom material from the user."""
    display_material_menu(database)

    material = input(
        "\nEnter material name or 'Custom': "
    ).strip()

    if material.lower() == "custom":
        material = input(
            "Enter custom material name: "
        ).strip()

        if not material:
            material = "Custom Material"

        yield_strength = get_validated_input(
            "Enter yield strength (MPa): ",
            validate_positive_number
        )

        youngs_modulus = get_validated_input(
            "Enter Young's modulus (GPa): ",
            validate_positive_number
        )

        database[material] = {
            "yield_strength": yield_strength,
            "youngs_modulus": youngs_modulus
        }

    return material


def run_calculation(
    material: str,
    database: dict,
    history: list,
    unique_materials: set
) -> None:
    """Run and store one complete calculation."""
    inputs = get_test_inputs()

    results = perform_calculation(
        material,
        inputs,
        database
    )

    record = create_calculation_record(
        material,
        inputs,
        results
    )

    add_to_history(history, record)
    unique_materials.add(material)

    display_calculation_results(
        record,
        database
    )


def main() -> None:
    """Run the modular stress and strain calculator."""
    database, history, unique_materials = setup_program()

    print("=== Stress and Strain Calculator ===")

    while True:
        try:
            material = handle_material(database)

            get_material_properties(
                material,
                database
            )

            run_calculation(
                material,
                database,
                history,
                unique_materials
            )

        except KeyError as error:
            print(f"  [Error]: {error}")

        again = input(
            "\nPerform another calculation? (y/n): "
        ).strip().lower()

        if again != "y":
            break

    display_session_summary(
        history,
        unique_materials
    )

    print(
        "\nExiting Stress and Strain Analysis System. "
        "Session closed."
    )


if __name__ == "__main__":
    main()