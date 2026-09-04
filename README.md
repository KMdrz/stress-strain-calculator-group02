# Stress and Strain Analysis System

## Group Members

| Group Member | Primary Responsibility                     |
| ------------ | ------------------------------------------ |
| **MADERAZO** | Task 1 – Basic Calculations                |
| **LLERA**    | Task 2 – Control Structures                |
| **CALVARIO** | Task 3 – Data Structures and Test History  |
| **FLORES**   | Task 4 – Functions and Parameters          |
| **VELARDE**  | Task 5 – Object-Oriented Programming (OOP) |

**Task 6 – Modular Integration was completed collaboratively by all members.**

---

## Project Description

The **Stress and Strain Analysis System** is a Python-based engineering application designed to calculate and analyze the mechanical behavior of different materials under applied forces.

The project was developed progressively across multiple tasks, beginning with basic stress and strain calculations and evolving into a modular, object-oriented system. The final version uses Python modules and classes to organize the program into separate components, making the system easier to maintain, extend, and reuse.

The system allows users to select existing materials or create custom materials, perform stress and strain tests, evaluate material safety, and manage test results.

---

## Program Features

The final application provides the following features:

* Calculate **stress** from applied force and cross-sectional area.
* Calculate **strain** from original length and change in length.
* Calculate the **observed Young's modulus**.
* Calculate the **factor of safety** based on material yield strength.
* Determine whether a test is **SAFE, CAUTION, or DANGER**.
* Identify the type of loading as **Tension** or **Compression**.
* Store material properties such as:

  * Density
  * Yield strength
  * Typical Young's modulus
* Support different material categories:

  * Metal
  * Plastic
  * Composite
  * General Material
* Allow users to create **custom materials**.
* Use object-oriented programming through classes, inheritance, properties, and special methods.
* Store and manage multiple stress-strain tests.
* Maintain a history of completed tests.
* Track unique materials used during a session.
* Generate a summary of test results.
* Save and load test results using **JSON**.
* Export test data using **CSV**.
* Timestamp tests using **datetime**.
* Manage file paths using **os/pathlib**.
* Generate simulated test data using **random**.
* Include validation and error handling for invalid inputs.

---

## Installation Requirements

### Python Version

**Python 3.13**

The project primarily uses Python's standard library, so no external packages are required.

The following standard library modules are used:

* `dataclasses`
* `typing`
* `json`
* `csv`
* `datetime`
* `pathlib`
* `random`
* `os`

These modules are included with Python and do not require separate installation.

### Installing Python

If Python is not installed, download and install Python from the official Python website.

After installation, verify that Python is available by running:

```bash
python --version
```

---

## How to Run the Program

Make sure Python is installed on your computer.

Open the project folder in a code editor such as **Visual Studio Code** or open a terminal/command prompt in the project folder.

Because the final program uses Python modules and package imports, run the program from the **root project folder** using:

```bash
python -m stress_calculator.main
```

The Python interpreter will execute the program and display the available materials and calculation options in the terminal.

Follow the prompts to:

1. Select an existing material or create a custom material.
2. Enter the applied force.
3. Enter the cross-sectional area.
4. Enter the original length.
5. Enter the change in length.
6. View the calculated stress, strain, Young's modulus, safety factor, and safety status.
7. Perform additional tests if needed.
8. View the test session summary when finished.

---

## Repository Structure

```text
stress-strain-calculator-group02/
│
├── README.md
├── Task1.py
├── Task2.py
├── Task3.py
├── Task4.py
├── Task5.py
│
└── stress_calculator/
    ├── __init__.py
    ├── material.py
    ├── properties.py
    ├── tests.py
    ├── utils.py
    ├── database.py
    └── main.py
```

| Module          | Description                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------- |
| `properties.py` | Defines the `MaterialProperties` dataclass and validates material properties.                 |
| `material.py`   | Implements the material hierarchy, including `Material`, `Metal`, `Plastic`, and `Composite`. |
| `tests.py`      | Defines `StressStrainTest` and `TestCollection` for calculations and test history.            |
| `utils.py`      | Provides utility functions for input validation, calculations, and conversions.               |
| `database.py`   | Creates and provides access to the standard material database and file storage features.      |
| `main.py`       | Connects all modules into the main interactive stress and strain analysis application.        |
| `__init__.py`   | Defines `stress_calculator` as a Python package.                                              |

---


