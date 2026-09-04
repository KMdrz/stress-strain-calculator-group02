def main() -> None:
    database = get_materials_database()
    collection = TestCollection()

    print("=== Stress and Strain Analysis System (Task 5: OOP) ===")

    while True:
        display_materials_menu(database)
        mat_input = input("\nEnter material name or 'Custom': ").strip()

        if mat_input.lower() == "custom":
            selected_material = handle_custom_material_creation()
            database[selected_material.name] = selected_material
        else:
            selected_material = get_material(mat_input, database)
            if not selected_material:
                print(f"  [Error]: Material '{mat_input}' not found in database.")
                continue

        force = prompt_non_zero_float("Enter applied force (N): ")
        area = prompt_positive_float("Enter cross-sectional area (m²): ")
        original_length = prompt_positive_float("Enter original length (m): ")
        change_in_length = prompt_non_zero_float("Enter change in length (m): ")

        try:
            test = StressStrainTest(
                material=selected_material,
                force=force,
                area=area,
                original_length=original_length,
                change_in_length=change_in_length
            )
            collection.add_test(test)

            print("\n=== Test Result ===")
            print(test)
            print(f"Loading Type: {test.loading_type}")
            print(f"Safety Factor: {test.safety_factor:.2f}")
            print(f"Safety Status: {test.safety_status}")
            print(f"Will Material Fail? {'Yes' if test.will_fail() else 'No'}")

        except ValueError as err:
            print(f"  [Error]: {err}")

        again = input("\nPerform another calculation? (y/n): ").strip().lower()
        if again != "y":
            break

    collection.display_summary()


if __name__ == "__main__":
    main()