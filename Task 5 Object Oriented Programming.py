class TestCollection:
    def __init__(self):
        self._history: List[StressStrainTest] = []
        self._unique_materials_used: Set[str] = set()


    def add_test(self, test: StressStrainTest) -> None:
        if test is None:
            return
        self._history.append(test)


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