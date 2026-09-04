# Task 2 Control Structures

def get_positive_float(prompt):
    """Gets a valid positive number from the user."""

    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Error: Value cannot be negative. Please try again.")

            elif value == 0:
                print(
                    "Error: Value must be greater than zero "
                    "to prevent division by zero."
                )

            else:
                return value

        except ValueError:
            print("Error: Please enter a valid numerical value.")

def get_force(prompt):
    """Gets a valid force value, including negative values for compression."""

    while True:
        try:
            value = float(input(prompt))

            if value == 0:
                print("Error: Force cannot be zero. Please try again.")
            else:
                return value

        except ValueError:
            print("Error: Please enter a valid numerical value.")


def select_material():
    """Allows the user to select a material."""

    while True:
        print("\n=== MATERIAL SELECTION ===")
        print("1. Steel")
        print("2. Aluminum")
        print("3. Titanium")
        print("4. Custom Material")

        choice = input("Select a material: ")

        if choice == "1":
            return "Steel", 250, 200

        elif choice == "2":
            return "Aluminum", 95, 69

        elif choice == "3":
            return "Titanium", 880, 114

        elif choice == "4":
            name = input("Enter custom material name: ")

            yield_strength = get_positive_float(
                "Enter yield strength (MPa): "
            )

            youngs_modulus = get_positive_float(
                "Enter Young's modulus (GPa): "
            )

            return name, yield_strength, youngs_modulus

        else:
            print("Error: Invalid choice. Please select 1-4.")


def main():
    """Main function for the stress and strain calculator."""

    print("=== Stress and Strain Calculator ===\n")

    while True:

        # Material selection
        material, yield_strength, youngs_modulus = select_material()

        print(f"\n=== Enter Test Data for {material} ===")

        force = get_force("Enter applied force: ")
        area = get_positive_float("Enter cross-sectional area: ")
        original_length = get_positive_float("Enter original length: ")
        change_in_length = get_positive_float(
            "Enter change in length: "
        )

        stress = force / area
        strain = change_in_length / original_length

        stress_mpa = stress / 1000000

        if stress_mpa > 0:
            loading = "Tension"
        else:
            loading = "Compression"

        factor_of_safety = yield_strength / abs(stress_mpa)

        if abs(stress_mpa) >= yield_strength:
            safety_status = "DANGER - Material is likely to fail."

        elif factor_of_safety < 1.25:
            safety_status = "CAUTION - Stress is close to yield strength."

        else:
            safety_status = "SAFE - Stress is below yield strength."

        print("\n=== RESULTS ===\n")

        # Material information
        print(f"Material: {material}")
        print(f"Yield Strength: {yield_strength:.2f} MPa")
        print(f"Young's Modulus: {youngs_modulus:.2f} GPa \n")


        print(f"Stress: {stress:.2f} Pa")
        print(f"Strain: {strain:.6f}")
        print(f"Stress (MPa): {stress_mpa:.2f}")
        print(f"Loading: {loading}")

        print(f"Factor of Safety: {factor_of_safety:.2f}")
        print(f"Safety Assessment: {safety_status}")

        print("\n=== Analysis Complete ===")
        1
        again = input(
            "\nDo you want to perform another calculation? "
            "(y/n): "
        ).strip().lower()

        if again != "y":
            print("\nThank you for using the Stress and Strain Calculator.")
            break


if __name__ == "__main__":
    main()