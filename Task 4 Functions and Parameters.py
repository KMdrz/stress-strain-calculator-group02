#Task 4 Functions and Parimeters

def display_material_menu(database):
    """Displays the available materials."""
    print("\nAvailable Materials:")

    for material in database:
        print(f"- {material}")


def display_calculation_results(record):
    """Displays the results of a calculation."""
    print("\n===== CALCULATION RESULTS =====")
    print(f"Material: {record['material']}")
    print(f"Force: {record['force']} N")
    print(f"Area: {record['area']} m²")
    print(f"Original Length: {record['original_length']} m")
    print(f"Change in Length: {record['change_in_length']} m")
    print(f"Stress: {record['stress_mpa']} MPa")
    print(f"Strain: {record['strain']}")
    print(f"Young's Modulus: {record['calc_modulus_gpa']} GPa")
    print(f"Factor of Safety: {record['safety_factor']}")
    print(f"Safety Status: {record['safety_status']}")


def display_safety_analysis(stress, yield_strength, safety_factor):
    """Displays the safety analysis."""
    print("\n===== SAFETY ANALYSIS =====")
    print(f"Applied Stress: {stress} MPa")
    print(f"Yield Strength: {yield_strength} MPa")
    print(f"Factor of Safety: {safety_factor}")


def display_session_summary(history, unique_materials):
    """Displays a summary of the calculation session."""
    print("\n===== SESSION SUMMARY =====")
    print(f"Total Calculations: {len(history)}")
    print(f"Unique Materials: {len(unique_materials)}")

    if history:
        highest_stress = max(history, key=lambda x: x["stress_mpa"])
        lowest_safety = min(history, key=lambda x: x["safety_factor"])
        average_strain = sum(record["strain"] for record in history) / len(history)

        print(f"Highest Stress: {highest_stress['stress_mpa']} MPa")
        print(f"Lowest Factor of Safety: {lowest_safety['safety_factor']}")
        print(f"Average Strain: {average_strain}"),