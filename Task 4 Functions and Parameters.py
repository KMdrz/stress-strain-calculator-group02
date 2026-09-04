#Task 4 Functions and Parameters

def setup_program():
    """Sets up the database and calculation history."""
    database = get_materials_database()
    history = []
    unique_materials = set()

    return database, history, unique_materials


def handle_material(database):
    """Gets the material selected by the user."""
    display_material_menu(database)
    material = input("\nEnter material name or 'Custom': ")

    if material.lower() == "custom":
        material = input("Enter custom material name: ")
        yield_strength = get_validated_input("Enter yield strength (MPa): ", validate_positive_number)
        youngs_modulus = get_validated_input("Enter Young's modulus (GPa): ", validate_positive_number)
        database[material] = {"yield_strength": yield_strength, "youngs_modulus": youngs_modulus}

    return material


def run_calculation(material, database, history, unique_materials):
    """Runs one complete calculation."""
    inputs = get_test_inputs()
    results = perform_calculation(material, inputs, database)
    record = create_calculation_record(material, inputs, results)

    add_to_history(history, record)
    unique_materials.add(material)
    display_calculation_results(record)


def main():
    """Runs the stress and strain calculator."""
    database, history, unique_materials = setup_program()

    while True:
        material = handle_material(database)
        try:
            get_material_properties(material, database)
        except KeyError:
            print("  [Error] Material not found.")
            continue

        run_calculation(material, database, history, unique_materials)

        again = input("\nPerform another calculation? (y/n): ")
        if again.lower() != "y":
            break

    display_session_summary(history, unique_materials)

if __name__ == "__main__":
    main()