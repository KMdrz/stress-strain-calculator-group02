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
        if self.area < 0:
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
            return float("inf")
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