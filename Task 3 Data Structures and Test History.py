# Task 3: Data Structures & Test History


def get_positive_float(prompt: str, allow_zero: bool = False) -> float:
    """Gets a valid positive number from the user."""
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


def get_force(prompt: str) -> float:
    """Gets a valid force value, including negative values for compression."""
    while True:
        try:
            value = float(input(prompt))

            if value == 0:
                print("  [Error]: Force cannot be zero. Please try again.")
            else:
                return value

        except ValueError:
            print("  [Error]: Please enter a valid numerical value.")


def main():
    """Main function for the stress and strain calculator."""

    print("=== Stress and Strain Calculator - Session Manager ===\n")

    # Data Structures
    calc_history = []
    unique_materials = set()

    # Fixed measurement units stored in a tuple
    units = ("N", "m²", "m", "Pa")

    # Material Database
    materials_db = {
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

    test_counter = 0

    # Session Loop
    while True:

        print("\nAvailable Materials in Database:")

        for mat, props in materials_db.items():
            print(
                f" - {mat} "
                f"(Yield: {props['yield_strength']} MPa, "
                f"E: {props['youngs_modulus']} GPa)"
            )

        print(" - Custom Material")

        mat_input = input(
            "\nEnter material name "
            "(or 'quit'/'exit' to finish session): "
        ).strip()

        # Exit Session
        if mat_input.lower() in ["quit", "exit", "q"]:
            break

        # Create case-insensitive lookup
        db_lookup = {}

        for key in materials_db:
            db_lookup[key.lower()] = key

        user_clean = mat_input.lower()

        try:

            # Material Selection
            if user_clean in ["custom", "custom material"]:

                mat_name = input(
                    "Enter custom material name: "
                ).strip().capitalize()

                if mat_name == "":
                    mat_name = "Custom Material"

                yield_strength = get_positive_float(
                    "Enter yield strength (MPa): "
                )

                youngs_modulus = get_positive_float(
                    "Enter Young's modulus (GPa): "
                )

                materials_db[mat_name] = {
                    "yield_strength": yield_strength,
                    "youngs_modulus": youngs_modulus
                }

            elif user_clean in db_lookup:

                mat_name = db_lookup[user_clean]

                yield_strength = materials_db[mat_name]["yield_strength"]
                youngs_modulus = materials_db[mat_name]["youngs_modulus"]

            else:

                raise KeyError(
                    f"Material '{mat_input}' not found in database!"
                )

            print(f"\n--- Enter Test Data for {mat_name} ---")

            # Measurement Inputs
            force = get_force(
                f"Enter applied force ({units[0]}): "
            )

            area = get_positive_float(
                f"Enter cross-sectional area ({units[1]}): "
            )

            original_length = get_positive_float(
                f"Enter original length ({units[2]}): "
            )

            change_in_length = get_positive_float(
                f"Enter change in length ({units[2]}): ",
                allow_zero=True
            )

            # Calculations
            stress = force / area
            strain = change_in_length / original_length
            stress_mpa = stress / 1_000_000

            # Loading Type
            if stress_mpa > 0:
                loading = "Tension"
            else:
                loading = "Compression"

            # Factor of Safety
            factor_of_safety = yield_strength / abs(stress_mpa)

            # Safety Analysis
            if abs(stress_mpa) >= yield_strength:

                safety_status = (
                    "DANGER / FAILURE - "
                    "Stress exceeds yield strength!"
                )

            elif factor_of_safety < 1.25:

                safety_status = (
                    f"CAUTION - "
                    f"Factor of Safety: {factor_of_safety:.2f}"
                )

            else:

                safety_status = (
                    f"SAFE - "
                    f"Factor of Safety: {factor_of_safety:.2f}"
                )

            test_counter += 1

            # Store Calculation in a Dictionary
            record = {
                "test_no": test_counter,
                "material": mat_name,
                "yield_strength": yield_strength,
                "youngs_modulus": youngs_modulus,
                "force": force,
                "area": area,
                "original_length": original_length,
                "change_in_length": change_in_length,
                "stress_pa": stress,
                "stress_mpa": stress_mpa,
                "strain": strain,
                "loading": loading,
                "safety_factor": factor_of_safety,
                "safety_status": safety_status
            }

            # Add Record to History List
            calc_history.append(record)

            # Add Material to Set
            unique_materials.add(mat_name)

            # Output Results
            print("\n=== RESULTS ===")
            print(f"Material: {mat_name}")
            print(f"Yield Strength: {yield_strength:.2f} MPa")
            print(f"Young's Modulus: {youngs_modulus:.2f} GPa")
            print()
            print(f"Stress: {stress:.2f} {units[3]}")
            print(f"Strain: {strain:.6f}")
            print(f"Stress (MPa): {stress_mpa:.2f}")
            print(f"Loading: {loading}")
            print(f"Safety Assessment: {safety_status}")

            print("\n=== Analysis Complete ===")

        except KeyError as e:

            print(f"  [Error]: {e.args[0]}")

    # ==========================================================
    # SESSION SUMMARY
    # ==========================================================

    print("\n====================================================")
    print("                SESSION SUMMARY REPORT")
    print("====================================================")

    total_calculations = len(calc_history)

    print(
        f"Total calculations performed : "
        f"{total_calculations}"
    )

    if unique_materials:
        materials_list = ", ".join(sorted(unique_materials))
    else:
        materials_list = "None"

    print(
        f"Unique materials tested "
        f"({len(unique_materials)}) : {materials_list}"
    )

    # Detailed Calculation History
    if calc_history:

        print("\n--- Detailed Calculation History ---")

        for rec in calc_history:

            print(
                f" Test #{rec['test_no']} "
                f"[{rec['material']}] | "
                f"Force: {rec['force']} N | "
                f"Stress: {rec['stress_mpa']:.2f} MPa | "
                f"Strain: {rec['strain']:.6f} | "
                f"Status: {rec['safety_status']}"
            )

        # ======================================================
        # STATISTICAL ANALYSIS
        # ======================================================

        print("\n--- Statistical Analysis ---")

        # Highest Stress
        max_stress_record = max(
            calc_history,
            key=lambda x: abs(x["stress_mpa"])
        )

        print(
            f" Highest Stress                  : "
            f"{max_stress_record['stress_mpa']:.2f} MPa "
            f"({max_stress_record['material']}, "
            f"Test #{max_stress_record['test_no']})"
        )

        # Lowest Factor of Safety
        min_safety_record = min(
            calc_history,
            key=lambda x: x["safety_factor"]
        )

        print(
            f" Lowest Factor of Safety         : "
            f"{min_safety_record['safety_factor']:.2f} "
            f"({min_safety_record['material']}, "
            f"Test #{min_safety_record['test_no']})"
        )

        # Average Strain
        total_strain = 0

        for rec in calc_history:
            total_strain += rec["strain"]

        avg_strain = total_strain / total_calculations

        print(
            f" Average Strain                  : "
            f"{avg_strain:.6f}"
        )

        # Best Stress-to-Strain Ratio
        best_ratio_record = min(
            calc_history,
            key=lambda x:
                abs(x["stress_mpa"]) / x["strain"]
                if x["strain"] != 0
                else float("inf")
        )

        if best_ratio_record["strain"] != 0:

            best_ratio = (
                abs(best_ratio_record["stress_mpa"])
                / best_ratio_record["strain"]
            )

            print(
                f" Best Stress-to-Strain Ratio     : "
                f"{best_ratio:.2f} "
                f"({best_ratio_record['material']}, "
                f"Test #{best_ratio_record['test_no']})"
            )

        else:

            print(
                " Best Stress-to-Strain Ratio     : "
                "Undefined (zero strain)"
            )

        # Failed Safety Checks
        failed_tests = []

        for rec in calc_history:

            if abs(rec["stress_mpa"]) >= rec["yield_strength"]:
                failed_tests.append(rec)

        print("\n--- Failed Safety Checks ---")

        if failed_tests:

            for rec in failed_tests:

                print(
                    f" - {rec['material']} "
                    f"(Test #{rec['test_no']}) | "
                    f"Stress: {rec['stress_mpa']:.2f} MPa | "
                    f"Yield Strength: "
                    f"{rec['yield_strength']:.2f} MPa"
                )

        else:

            print(" None")

    print(
        "\nExiting Stress and Strain Analysis System. "
        "Session closed."
    )


if __name__ == "__main__":
    main()