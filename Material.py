# material.py

from properties import MaterialProperties


class Material:
    """Base class for all materials."""

    def __init__(
        self,
        name: str,
        properties: MaterialProperties
    ):
        self.name = name.strip()
        self.properties = properties

    @property
    def yield_strength(self) -> float:
        """Return yield strength in MPa."""
        return self.properties.yield_strength

    @property
    def youngs_modulus(self) -> float:
        """Return typical Young's modulus in GPa."""
        return self.properties.typical_youngs_modulus

    @property
    def yield_strength_pa(self) -> float:
        """Return yield strength in Pa."""
        return self.yield_strength * 1_000_000

    @property
    def youngs_modulus_pa(self) -> float:
        """Return Young's modulus in Pa."""
        return self.youngs_modulus * 1_000_000_000

    def get_category(self) -> str:
        """Return the material category."""
        return "General Material"

    def can_withstand_stress(self, stress: float) -> bool:
        """Check whether the material can withstand a stress in MPa."""
        return abs(stress) < self.yield_strength

    def __str__(self) -> str:
        return (
            f"{self.name} [{self.get_category()}] "
            f"(Yield: {self.yield_strength:.1f} MPa, "
            f"E: {self.youngs_modulus:.1f} GPa)"
        )


class Metal(Material):
    """Represents a metal material."""

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
        """Return ductility percentage."""
        return self._ductility_pct

    @ductility_pct.setter
    def ductility_pct(self, value: float) -> None:
        if value < 0:
            raise ValueError("Ductility cannot be negative.")

        self._ductility_pct = value

    def get_category(self) -> str:
        return "Metal"


class Plastic(Material):
    """Represents a plastic material."""

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
    """Represents a composite material."""

    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        fiber_type: str = "Carbon Fiber"
    ):
        super().__init__(name, properties)

        self._fiber_type = (
            fiber_type.strip() or "Unspecified Fiber"
        )

    @property
    def fiber_type(self) -> str:
        """Return fiber type."""
        return self._fiber_type

    @fiber_type.setter
    def fiber_type(self, value: str) -> None:
        self._fiber_type = (
            value.strip() or "Unspecified Fiber"
        )

    def get_category(self) -> str:
        return "Composite"