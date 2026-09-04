# utils.py

import csv
import json
import random
from datetime import datetime
from pathlib import Path

from .test import StressStrainTest, TestCollection
from .material import Material


DATA_FOLDER = Path("data")


def calculate_stress(
    force: float,
    area: float
) -> float:
    """Calculate stress in Pa."""
    return force / area


def calculate_strain(
    original_length: float,
    change_in_length: float
) -> float:
    """Calculate strain."""
    return change_in_length / original_length


def calculate_youngs_modulus(
    stress: float,
    strain: float
) -> float:
    """Calculate Young's modulus."""
    if strain == 0:
        return 0.0

    return stress / strain


def ensure_data_folder() -> None:
    """Create the data folder if it does not exist."""
    DATA_FOLDER.mkdir(exist_ok=True)


def save_tests_to_json(
    collection: TestCollection,
    filename: str = "test_results.json"
) -> None:
    """Save test results to a JSON file."""

    ensure_data_folder()

    filepath = DATA_FOLDER / filename

    data = [
        test.to_dict()
        for test in collection
    ]

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            data,
            file,
            indent=4
        )

    print(f"Test results saved to {filepath}")


def load_tests_from_json(
    filename: str = "test_results.json"
) -> list:
    """Load test results from a JSON file."""

    filepath = DATA_FOLDER / filename

    if not filepath.exists():
        print(
            f"No saved file found at {filepath}"
        )
        return []

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


def export_tests_to_csv(
    collection: TestCollection,
    filename: str = "test_results.csv"
) -> None:
    """Export test results to CSV."""

    ensure_data_folder()

    filepath = DATA_FOLDER / filename

    if not collection:
        print("No test data available to export.")
        return

    records = [
        test.to_dict()
        for test in collection
    ]

    fieldnames = list(records[0].keys())

    with open(
        filepath,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(records)

    print(f"Test data exported to {filepath}")


def create_timestamp() -> str:
    """Create a timestamp for a test."""
    return datetime.now().isoformat(
        timespec="seconds"
    )


def generate_simulated_test(
    material: Material
) -> StressStrainTest:
    """Generate a random simulated stress-strain test."""

    force = random.choice([-1, 1]) * random.uniform(
        1000,
        100000
    )

    area = random.uniform(
        0.001,
        0.01
    )

    original_length = random.uniform(
        0.05,
        1.0
    )

    change_in_length = random.choice([-1, 1]) * random.uniform(
        0.0001,
        0.01
    )

    return StressStrainTest(
        material=material,
        force=force,
        area=area,
        original_length=original_length,
        change_in_length=change_in_length,
        timestamp=create_timestamp()
    )