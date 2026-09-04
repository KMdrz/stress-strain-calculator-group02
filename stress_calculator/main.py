# main.py

from .database import (
    get_materials_database,
    get_material,
    add_material
)

from .material import (
    Material,
    Metal,
    Plastic,
    Composite
)

from .properties import MaterialProperties

from .test import (
    StressStrainTest,
    TestCollection
)

from .utils import (
    save_tests_to_json,
    load_tests_from_json,
    export_tests_to_csv,
    generate_simulated_test
)


def prompt_positive_float(prompt_text: str) -> float:
    """Get a positive number from the user."""

    while True:
        try:
            value = float(input(prompt_text))

            if value <= 0:
                print(
                    "[Error]: Value must be greater than zero."
                )
                continue

            return value

        except ValueError:
            print(
                "[Error]: Invalid numerical input."
            )


def prompt_non_zero_float(prompt_text: str) -> float:
    """Get a non-zero number from the user."""

    while True:
        try:
            value = float(input(prompt_text))

            if value == 0:
                print(
                    "[Error]: Value cannot be zero."
                )
                continue

            return value

        except ValueError:
            print(
                "[Error]: Invalid numerical input."
            )


def display_materials_menu(
    database: dict
) -> None:
    """Display available materials."""

    print("\nAvailable Materials:")

    for material in database.values():
        print(f"- {material}")

    print("- Custom")


def handle_custom_material_creation() -> Material:
    """Create a custom material."""

    name = (
        input("Enter custom material name: ")
        .strip()
        or "Custom Material"
    )

    print("\nSelect Material Category:")
    print("1. Metal")
    print("2. Plastic")
    print("3. Composite")
    print("4. General Material")

    category = input(
        "Choice (1-4): "
    ).strip()

    density = prompt_positive_float(
        "Enter density (kg/m³): "
    )

    yield_strength = prompt_positive_float(
        "Enter yield strength (MPa): "
    )

    youngs_modulus = prompt_positive_float(
        "Enter Young's modulus (GPa): "
    )

    properties = MaterialProperties(
        density,
        yield_strength,
        youngs_modulus
    )

    if category == "1":
        ductility = prompt_positive_float(
            "Enter ductility (% elongation): "
        )

        return Metal(
            name,
            properties,
            ductility
        )

    if category == "2":
        is_thermoplastic = (
            input(
                "Is it thermoplastic? (y/n): "
            ).strip().lower()
            == "y"
        )

        return Plastic(
            name,
            properties,
            is_thermoplastic
        )

    if category == "3":
        fiber = (
            input("Enter fiber type: ")
            .strip()
            or "Fiberglass"
        )

        return Composite(
            name,
            properties,
            fiber
        )

    return Material(
        name,
        properties
    )


def run_manual_test(
    selected_material: Material,
    collection: TestCollection
) -> None:
    """Run one manual stress-strain test."""

    force = prompt_non_zero_float(
        "Enter applied force (N): "
    )

    area = prompt_positive_float(
        "Enter cross-sectional area (m²): "
    )

    original_length = prompt_positive_float(
        "Enter original length (m): "
    )

    change_in_length = prompt_non_zero_float(
        "Enter change in length (m): "
    )

    try:
        test = StressStrainTest(
            material=selected_material,
            force=force,
            area=area,
            original_length=original_length,
            change_in_length=change_in_length
        )

        collection.add_test(test)

        display_test_result(test)

    except ValueError as error:
        print(f"[Error]: {error}")


def display_test_result(
    test: StressStrainTest
) -> None:
    """Display the result of one test."""

    print("\n=== TEST RESULT ===")
    print(f"Material: {test.material.name}")
    print(f"Timestamp: {test.timestamp}")
    print(f"Loading Type: {test.loading_type}")
    print(f"Stress = {test.stress_pa:,.0f} Pa")
    print(f"Strain: {test.strain:.4f}")
    print(
        f"Young's Modulus: "
        f"{test.calculated_modulus_gpa:.2f} GPa"
    )
    print(
        f"Safety Factor: "
        f"{test.safety_factor:.2f}"
    )
    print(
        f"Safety Status: "
        f"{test.safety_status}"
    )
    print(
        f"Will Material Fail? "
        f"{'Yes' if test.will_fail() else 'No'}"
    )


def run_simulated_test(
    database: dict,
    collection: TestCollection
) -> None:
    """Generate a random simulated test."""

    materials = list(database.values())

    if not materials:
        print("No materials available.")
        return

    import random

    selected_material = random.choice(materials)

    test = generate_simulated_test(
        selected_material
    )

    collection.add_test(test)

    print("\n=== SIMULATED TEST ===")
    display_test_result(test)


def main() -> None:
    """Run the modular stress and strain calculator."""

    database = get_materials_database()
    collection = TestCollection()

    print(
        "=== Stress and Strain Analysis System ==="
    )

    while True:

        print("\n--- Main Menu ---")
        print("1. Perform manual test")
        print("2. Generate simulated test")
        print("3. Display session summary")
        print("4. Save results to JSON")
        print("5. Load JSON results")
        print("6. Export results to CSV")
        print("7. Exit")

        choice = input(
            "\nEnter choice (1-7): "
        ).strip()

        if choice == "1":

            display_materials_menu(database)

            mat_input = input(
                "\nEnter material name or 'Custom': "
            ).strip()

            if mat_input.lower() == "custom":

                selected_material = (
                    handle_custom_material_creation()
                )

                add_material(
                    selected_material,
                    database
                )

            else:

                selected_material = get_material(
                    mat_input,
                    database
                )

                if not selected_material:
                    print(
                        f"[Error]: Material "
                        f"'{mat_input}' not found."
                    )
                    continue

            run_manual_test(
                selected_material,
                collection
            )

        elif choice == "2":

            run_simulated_test(
                database,
                collection
            )

        elif choice == "3":

            collection.display_summary()

        elif choice == "4":

            save_tests_to_json(
                collection
            )

        elif choice == "5":

            loaded_data = load_tests_from_json()

            if loaded_data:
                print(
                    f"\nLoaded {len(loaded_data)} "
                    f"saved test(s)."
                )

                for record in loaded_data:
                    print(
                        f"- {record['material']}: "
                        f"{record['stress_mpa']:.2f} MPa "
                        f"({record['timestamp']})"
                    )

        elif choice == "6":

            export_tests_to_csv(
                collection
            )

        elif choice == "7":

            print(
                "\nExiting Stress and Strain "
                "Analysis System."
            )
            break

        else:

            print(
                "[Error]: Invalid choice. "
                "Please enter 1-7."
            )


if __name__ == "__main__":
    main()