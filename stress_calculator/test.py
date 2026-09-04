# tests.py

from dataclasses import dataclass
from typing import List, Set, Iterator

from .material import Material
from datetime import datetime


@dataclass
class StressStrainTest:
    """Represents one stress-strain test."""

    material: Material
    force: float
    area: float
    original_length: float
    change_in_length: float
    timestamp: str = ""

    def __post_init__(self):
        if self.force == 0:
            raise ValueError("Applied force cannot be zero.")

        if self.area <= 0:
            raise ValueError("Area must be greater than zero.")

        if self.original_length <= 0:
            raise ValueError(
                "Original length must be greater than zero."
            )

        if self.change_in_length == 0:
            raise ValueError(
                "Change in length cannot be zero."
            )

        if not self.timestamp:
            self.timestamp = datetime.now().isoformat(
                timespec="seconds"
            )

    @property
    def stress_pa(self) -> float:
        """Calculate stress in Pa."""
        return self.force / self.area

    @property
    def stress_mpa(self) -> float:
        """Calculate stress in MPa."""
        return self.stress_pa / 1_000_000

    @property
    def strain(self) -> float:
        """Calculate strain."""
        return self.change_in_length / self.original_length

    @property
    def calculated_modulus_gpa(self) -> float:
        """Calculate observed Young's modulus in GPa."""
        current_strain = self.strain

        if current_strain == 0:
            return 0.0

        return (
            abs(self.stress_pa / current_strain)
            / 1_000_000_000
        )

    @property
    def safety_factor(self) -> float:
        """Calculate factor of safety."""
        current_stress_mpa = abs(self.stress_mpa)

        if current_stress_mpa == 0:
            return float("inf")

        return (
            self.material.yield_strength
            / current_stress_mpa
        )

    @property
    def safety_status(self) -> str:
        """Return the safety status of the test."""

        if not self.material.can_withstand_stress(
            self.stress_mpa
        ):
            return "DANGER"

        if self.safety_factor < 1.25:
            return "CAUTION"

        return "SAFE"

    @property
    def loading_type(self) -> str:
        """Return tension or compression."""
        return (
            "Tension"
            if self.force > 0
            else "Compression"
        )

    def will_fail(self) -> bool:
        """Determine whether the material is likely to fail."""
        return not self.material.can_withstand_stress(
            self.stress_mpa
        )

    def to_dict(self) -> dict:
        """Convert the test into a dictionary."""
        return {
            "timestamp": self.timestamp,
            "material": self.material.name,
            "category": self.material.get_category(),
            "force": self.force,
            "area": self.area,
            "original_length": self.original_length,
            "change_in_length": self.change_in_length,
            "stress_pa": self.stress_pa,
            "stress_mpa": self.stress_mpa,
            "strain": self.strain,
            "calculated_modulus_gpa":
                self.calculated_modulus_gpa,
            "safety_factor": self.safety_factor,
            "safety_status": self.safety_status,
            "loading_type": self.loading_type
        }

    def __str__(self) -> str:
        return (
            f"Test on {self.material.name}: "
            f"Stress={self.stress_mpa:.2f} MPa, "
            f"Strain={self.strain:.6f}, "
            f"Young's Modulus="
            f"{self.calculated_modulus_gpa:.2f} GPa"
        )

    def __lt__(
        self,
        other: "StressStrainTest"
    ) -> bool:
        """Allow tests to be sorted by stress."""
        return self.stress_mpa < other.stress_mpa


class TestCollection:
    """Stores and analyzes multiple stress-strain tests."""

    def __init__(self):
        self._history: List[StressStrainTest] = []
        self._unique_materials_used: Set[str] = set()

    def add_test(
        self,
        test: StressStrainTest
    ) -> None:
        """Add a test to the collection."""
        self._history.append(test)
        self._unique_materials_used.add(
            test.material.name
        )

    @property
    def history(self) -> List[StressStrainTest]:
        """Return a copy of the test history."""
        return list(self._history)

    @property
    def unique_materials_used(self) -> Set[str]:
        """Return a copy of the material set."""
        return set(self._unique_materials_used)

    def __len__(self) -> int:
        return len(self._history)

    def __iter__(
        self
    ) -> Iterator[StressStrainTest]:
        return iter(self._history)

    def __bool__(self) -> bool:
        return bool(self._history)

    def display_summary(self) -> None:
        """Display the session summary."""

        print("\n=== TEST SESSION SUMMARY ===")
        print(f"Total Tests: {len(self)}")
        print(
            f"Materials Tested: "
            f"{len(self._unique_materials_used)}"
        )

        if not self._history:
            print("No tests performed in this session.")
            return

        highest_stress = max(
            self._history,
            key=lambda test: abs(test.stress_mpa)
        )

        lowest_safety = min(
            self._history,
            key=lambda test: test.safety_factor
        )

        average_strain = (
            sum(test.strain for test in self._history)
            / len(self._history)
        )

        failed_tests = [
            test
            for test in self._history
            if test.safety_status == "DANGER"
        ]

        print("\n--- Statistical Analysis ---")

        print(
            f"Highest Stress: "
            f"{highest_stress.stress_mpa:.2f} MPa "
            f"({highest_stress.material.name})"
        )

        print(
            f"Lowest Factor of Safety: "
            f"{lowest_safety.safety_factor:.2f} "
            f"({lowest_safety.material.name})"
        )

        print(
            f"Average Strain: "
            f"{average_strain:.6f}"
        )

        print("\n--- Failed Safety Checks ---")

        if failed_tests:
            for test in failed_tests:
                print(
                    f"- {test.material.name}: "
                    f"{test.stress_mpa:.2f} MPa"
                )
        else:
            print("None")

        print("\n--- Detailed Test History ---")

        for test in self._history:
            print(
                f"- {test.material.name}: "
                f"Stress={test.stress_mpa:.2f} MPa, "
                f"Strain={test.strain:.6f}, "
                f"Safety Factor="
                f"{test.safety_factor:.2f}, "
                f"Status={test.safety_status}"
            )