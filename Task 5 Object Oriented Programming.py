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