# Task 3: Data Structures & Test History

def main():
    print("=== Stress and Strain Calculator - Session Manager ===")

    calc_history = []

    materials_db = {
        "Steel": {"yield_strength": 250.0, "youngs_modulus": 200.0},
        "Aluminum": {"yield_strength": 95.0, "youngs_modulus": 69.0}
    }

    while True:
        mat_input = input("\nEnter material name (or 'quit' to exit): ").strip()
        if mat_input.lower() == 'quit':
            break

        if mat_input in materials_db:
            yield_strength = materials_db[mat_input]["yield_strength"]
            youngs_modulus = materials_db[mat_input]["youngs_modulus"]
        else:
            print("Material not found!")
            continue

        force = float(input("Enter applied force (N): "))
        area = float(input("Enter cross-sectional area (m²): "))
        original_length = float(input("Enter original length (m): "))
        change_in_length = float(input("Enter change in length (m): "))

        stress = force / area
        strain = change_in_length / original_length
        stress_mpa = stress / 1_000_000

        print("\n=== RESULTS ===")
        print(f"Material: {mat_input}")
        print(f"Stress: {stress:.2f} Pa")
        print(f"Strain: {strain:.2f}")
        print(f"Stress (MPa): {stress_mpa:.2f}")

if __name__ == "__main__":
    main()