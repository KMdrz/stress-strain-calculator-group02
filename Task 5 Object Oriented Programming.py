def display_materials_menu(database: Dict[str, Material]) -> None:
    print("\nAvailable Materials:")
    for material in database.values():
        print(f"- {material}")
    print("- Custom")


def handle_custom_material_creation() -> Material:
    name = input("Enter custom material name: ").strip() or "Custom Material"

    print("\nSelect Material Category:")
    print("1. Metal")
    print("2. Plastic")
    print("3. Composite")
    print("4. General Material")

    cat_choice = input("Choice (1-4): ")

    density = prompt_positive_float("Enter density (kg/m³): ")
    yield_strength = prompt_positive_float("Enter yield strength (MPa): ")
    youngs_modulus = prompt_positive_float("Enter Young's modulus (GPa): ")

    properties = MaterialProperties(density, yield_strength, youngs_modulus)

    if cat_choice == "1":
        ductility = prompt_positive_float("Enter ductility (% elongation): ")
        return Metal(name, properties)

    elif cat_choice == "2":
        is_thermo = input("Is it thermoplastic? (y/n): ").strip().lower() == "y"
        return Plastic(name, properties)

    elif cat_choice == "3":
        fiber = input("Enter fiber type: ").strip() or "Fiberglass"
        return Composite(name, properties)

    return Material(name, properties)