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
        self._fiber_type = fiber_type.strip()

        if self._fiber_type == "":
            self._fiber_type = "Unspecified Fiber"

    @property
    def fiber_type(self) -> str:
        return self._fiber_type

    @fiber_type.setter
    def fiber_type(self, value: str) -> None:
        self._fiber_type = value.strip()

        if self._fiber_type == "":
            self._fiber_type = "Unspecified Fiber"

    def get_category(self) -> str:
        return "Composite"