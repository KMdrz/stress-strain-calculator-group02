# Task 5 OOP

from dataclasses import dataclass
from typing import Dict, List, Set, Optional, Iterator

@dataclass
class MaterialProperties:
    density: float
    yield_strength: float
    typical_youngs_modulus: float

    def __post_init__(self):
        if self.density <= 0:
            raise ValueError("Density must be greater than zero.")
        if self.yield_strength <= 0:
            raise ValueError("Yield strength must be greater than zero.")
        if self.typical_youngs_modulus <= 0:
            raise ValueError("Young's modulus must be greater than zero.")


class Material:
    def __init__(
        self,
        name: str,
        properties: MaterialProperties
    ):
        self.name = name.strip()
        self.properties = properties

    @property
    def yield_strength(self) -> float:
        return self.properties.yield_strength

    @property
    def youngs_modulus(self) -> float:
        return self.properties.typical_youngs_modulus

    @property
    def yield_strength_pa(self) -> float:
        return self.yield_strength * 1_000_000

    @property
    def youngs_modulus_pa(self) -> float:
        return self.youngs_modulus * 1_000_000_000

    def get_category(self) -> str:
        return "General Material"

    def can_withstand_stress(self, stress: float) -> bool:
        return abs(stress) < self.yield_strength

    def __str__(self) -> str:
        return (
            f"{self.name} [{self.get_category()}] "
            f"(Yield: {self.yield_strength:.1f} MPa, "
            f"E: {self.youngs_modulus:.1f} GPa)"
        )


class Metal(Material):
    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        ductility_pct: float = 15.0
    ):
        super().__init__(name, properties)
        self._ductility_pct = 0.0
        self.ductility_pct = ductility_pct

    @property
    def ductility_pct(self) -> float:
        return self._ductility_pct

    @ductility_pct.setter
    def ductility_pct(self, value: float) -> None:
        if value < 0:
            raise ValueError("Ductility cannot be negative.")
        self._ductility_pct = value

    def get_category(self) -> str:
        return "Metal"


class Plastic(Material):
    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        is_thermoplastic: bool = True
    ):
        super().__init__(name, properties)
        self.is_thermoplastic = is_thermoplastic

    def get_category(self) -> str:
        return "Plastic"


class Composite(Material):
    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        fiber_type: str = "Carbon Fiber"
    ):
        super().__init__(name, properties)
        self._fiber_type = fiber_type.strip() or "Unspecified Fiber"

    @property
    def fiber_type(self) -> str:
        return self._fiber_type

    @fiber_type.setter
    def fiber_type(self, value: str) -> None:
        self._fiber_type = value.strip() or "Unspecified Fiber"

    def get_category(self) -> str:
        return "Composite"


@dataclass
class StressStrainTest:
    material: Material
    force: float
    area: float
    original_length: float
    change_in_length: float

    def __post_init__(self):
        if self.force == 0:
            raise ValueError("Applied force cannot be zero.")
        if self.area <= 0:
            raise ValueError("Area must be greater than zero.")
        if self.original_length <= 0:
            raise ValueError("Original length must be greater than zero.")
        if self.change_in_length == 0:
            raise ValueError("Change in length cannot be zero.")

    @property
    def stress_pa(self) -> float:
        return self.force / self.area

    @property
    def stress_mpa(self) -> float:
        return self.stress_pa / 1_000_000

    @property
    def strain(self) -> float:
        if self.original_length == 0:
            return 0.0
        return self.change_in_length / self.original_length

    @property
    def calculated_modulus_gpa(self) -> float:
        current_strain = self.strain
        if current_strain == 0:
            return 0.0
        return abs(self.stress_pa / current_strain) / 1_000_000_000

    @property
    def safety_factor(self) -> float:
        current_stress_mpa = abs(self.stress_mpa)
        if current_stress_mpa == 0:
            return float('inf')
        return self.material.yield_strength / current_stress_mpa

    @property
    def safety_status(self) -> str:
        if not self.material.can_withstand_stress(self.stress_mpa):
            return "DANGER"
        elif self.safety_factor < 1.25:
            return "CAUTION"
        return "SAFE"

    @property
    def loading_type(self) -> str:
        return "Tension" if self.force > 0 else "Compression"

    def will_fail(self) -> bool:
        return not self.material.can_withstand_stress(self.stress_mpa)

    def __str__(self) -> str:
        return (
            f"Test on {self.material.name}: "
            f"Stress={self.stress_mpa:.2f} MPa, "
            f"Strain={self.strain:.6f}, "
            f"Young's Modulus={self.calculated_modulus_gpa:.2f} GPa"
        )

    def __lt__(self, other: "StressStrainTest") -> bool:
        """Enables sorting tests by stress (used by TestCollection)."""
        return self.stress_mpa < other.stress_mpa


class TestCollection:
    def __init__(self):
        self._history: List[StressStrainTest] = []
        self._unique_materials_used: Set[str] = set()


    def add_test(self, test: StressStrainTest) -> None:
        self._history.append(test)
        self._unique_materials_used.add(test.material.name)


    @property
    def history(self) -> List[StressStrainTest]:
        return list(self._history)


    @property
    def unique_materials_used(self) -> Set[str]:
        return set(self._unique_materials_used)

    def __len__(self) -> int:
        return len(self._history)

    def __iter__(self) -> Iterator[StressStrainTest]:
        return iter(self._history)

    def __bool__(self) -> bool:
        return bool(self._history)

    def display_summary(self) -> None:
        print("\n=== Test Session Summary ===")
        print(f"Total tests: {len(self)}")
        print(f"Materials tested: {len(self._unique_materials_used)}")

        if self._history:
            print("\n--- Detailed Test History ---")
            for test in self._history:
                print(
                    f"- {test.material.name}: "
                    f"Stress={test.stress_mpa:.2f} MPa, "
                    f"Strain={test.strain:.6f}, "
                    f"Young's Modulus={test.calculated_modulus_gpa:.2f} GPa, "
                    f"Safety Factor={test.safety_factor:.2f}, "
                    f"Status={test.safety_status}"
                )
        else:
            print("No tests performed in this session.")


def get_materials_database() -> Dict[str, Material]:
    steel = MaterialProperties(7850, 250.0, 200.0)
    aluminum = MaterialProperties(2700, 95.0, 69.0)
    titanium = MaterialProperties(4500, 880.0, 114.0)
    polycarbonate_props = MaterialProperties(1200, 62.0, 2.3)
    carbon_fiber_props = MaterialProperties(1600, 600.0, 150.0)

    return {
        "Steel": Metal("Steel", steel, 15.0),
        "Aluminum": Metal("Aluminum", aluminum, 25.0),
        "Titanium": Metal("Titanium", titanium, 10.0),
        "Polycarbonate": Plastic("Polycarbonate", polycarbonate_props),
        "Carbon Fiber": Composite("Carbon Fiber", carbon_fiber_props, "3K Carbon")
    }


def get_material(name: str, database: Dict[str, Material]) -> Optional[Material]:
    db_lookup = {key.lower(): key for key in database}
    cleaned_name = name.strip().lower()

    if cleaned_name in db_lookup:
        return database[db_lookup[cleaned_name]]

    return None


def prompt_positive_float(prompt_text: str) -> float:
    while True:
        try:
            value = float(input(prompt_text))
            if value <= 0:
                print("  [Error]: Value must be greater than zero.")
                continue
            return value
        except ValueError:
            print("  [Error]: Invalid numerical input. Try again.")


def prompt_non_zero_float(prompt_text: str) -> float:
    while True:
        try:
            value = float(input(prompt_text))
            if value == 0:
                print("  [Error]: Value cannot be zero.")
                continue
            return value
        except ValueError:
            print("  [Error]: Invalid numerical input. Try again.")


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

    cat_choice = input("Choice (1-4): ").strip()

    density = prompt_positive_float("Enter density (kg/m³): ")
    yield_strength = prompt_positive_float("Enter yield strength (MPa): ")
    youngs_modulus = prompt_positive_float("Enter Young's modulus (GPa): ")

    properties = MaterialProperties(density, yield_strength, youngs_modulus)

    if cat_choice == "1":
        ductility = prompt_positive_float("Enter ductility (% elongation): ")
        return Metal(name, properties, ductility_pct=ductility)

    elif cat_choice == "2":
        is_thermo = input("Is it thermoplastic? (y/n): ").strip().lower() == "y"
        return Plastic(name, properties, is_thermoplastic=is_thermo)

    elif cat_choice == "3":
        fiber = input("Enter fiber type: ").strip() or "Fiberglass"
        return Composite(name, properties, fiber_type=fiber)

    return Material(name, properties)


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