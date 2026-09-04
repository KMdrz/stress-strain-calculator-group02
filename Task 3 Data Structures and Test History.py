# Task 3: Data Structures & Test History

def get_positive_float(prompt: str, allow_zero: bool = False) -> float:
    """Gets a valid positive number from the user using Task 2 validation rules."""
    while True:
        try:
            value = float(input(prompt))
            if allow_zero and value == 0:
                return value
            if value < 0:
                print("  [Error]: Value cannot be negative. Please try again.")
            elif not allow_zero and value == 0:
                print("  [Error]: Value must be greater than zero. Please try again.")
            else:
                return value
        except ValueError:
            print("  [Error]: Please enter a valid numerical value.")

def main():
    print("=== Stress and Strain Calculator - Session Manager ===\n")

    calc_history = []
    unique_materials = set()
    units = ("N", "m²", "m", "Pa")

    materials_db = {
        "Steel": {"yield_strength": 250.0, "youngs_modulus": 200.0},
        "Aluminum": {"yield_strength": 95.0, "youngs_modulus": 69.0},
        "Titanium": {"yield_strength": 880.0, "youngs_modulus": 114.0}
    }

    test_counter = 0

    while True:
        print("\nAvailable Materials in Database:")
        for mat, props in materials_db.items():
            print(f" - {mat} (Yield: {props['yield_strength']} MPa, E: {props['youngs_modulus']} GPa)")
        print(" - Custom Material")

        mat_input = input("\nEnter material name (or 'quit'/'exit' to finish session): ").strip()

        if mat_input.lower() in ['quit', 'exit', 'q']:
            break

        db_lookup = {k.lower(): k for k in materials_db.keys()}
        user_clean = mat_input.lower()

        try:
            if user_clean == "custom" or user_clean == "custom material":
                mat_name = input("Enter custom material name: ").strip().capitalize() or "Custom Material"
                yield_strength = get_positive_float("Enter yield strength (MPa): ")
                youngs_modulus = get_positive_float("Enter Young's modulus (GPa): ")

                materials_db[mat_name] = {
                    "yield_strength": yield_strength,
                    "youngs_modulus": youngs_modulus
                }
            elif user_clean in db_lookup:
                mat_name = db_lookup[user_clean]
                yield_strength = materials_db[mat_name]["yield_strength"]
                youngs_modulus = materials_db[mat_name]["youngs_modulus"]
            else:
                raise KeyError(f"Material '{mat_input}' not found in database!")

            print(f"\n--- Enter Test Data for {mat_name} ---")

            force = get_positive_float(f"Enter applied force ({units[0]}): ")
            area = get_positive_float(f"Enter cross-sectional area ({units[1]}): ")
            original_length = get_positive_float(f"Enter original length ({units[2]}): ")
            change_in_length = get_positive_float(f"Enter change in length ({units[2]}): ", allow_zero=True)

            stress = force / area
            strain = change_in_length / original_length
            stress_mpa = stress / 1_000_000

            print("\n=== RESULTS ===")
            print(f"Material: {mat_name}")
            print(f"Stress: {stress:.2f} {units[3]}")
            print(f"Strain: {strain:.6f}")
            print(f"Stress (MPa): {stress_mpa:.2f}")

        except KeyError as e:
            print(f"  [Error]: {e.args[0]}")

if __name__ == "__main__":
    main()