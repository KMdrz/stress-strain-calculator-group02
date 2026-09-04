Group Members
Group Member
Primary Responsibility
MADERAZO | Task 1
Basic Calculations
LLERA | Task 2
Control Structures
CALVARIO | Task 3
Data Structures and Test History
FLORES | Task 4
Functions and Parameters
VELARDE | Task 5
Object-Oriented Programming (OOP)
Task 6 – Modular Integration was completed collaboratively by all members.


Project Description
The Stress and Strain Analysis System is a Python-based engineering application designed to calculate and analyze the mechanical behavior of different materials under applied forces.

The project was developed progressively across multiple tasks, beginning with basic stress and strain calculations and evolving into a modular, object-oriented system. The final version uses Python modules and classes to organize the program into separate components, making the system easier to maintain, extend, and reuse.

The system allows users to select existing materials or create custom materials, perform stress and strain tests, evaluate material safety, and manage test results.


Program Features
The final application provides the following features:
Calculate stress from applied force and cross-sectional area.
Calculate strain from original length and change in length.
Calculate the observed Young's modulus.
Calculate the factor of safety based on material yield strength.
Determine whether a test is SAFE, CAUTION, or DANGER.
Identify the type of loading as Tension or Compression.
Store material properties such as:
Density
Yield strength
Typical Young's modulus
Support different material categories:
Metal
Plastic
Composite
General Material
Allow users to create custom materials.
Use object-oriented programming through classes, inheritance, properties, and special methods.
Store and manage multiple stress-strain tests.
Maintain a history of completed tests.
Track unique materials used during a session.
Generate a summary of test results.
Save and load test results using JSON.
Export test data using CSV.
Timestamp tests using datetime.
Manage file paths using os/pathlib.
Generate simulated test data using random. 
Include validation and error handling for invalid inputs.



Installation Requirements
Python Version: Python 3.13

The project primarily uses Python's standard library, so no external packages are required.

The following standard library modules are used:
`dataclasses`
`typing`
`json`
`csv`
`datetime`
`pathlib`
`random`
`os`

These modules are included with Python and do not require separate installation.

Installing Python

If Python is not installed, download and install Python from the official Python website.

After installation, verify that Python is available by running:
```bash
python --version





How To Run The Program
To run the python program, make sure that python is installed on your computer. Open the code editor such as visual code or the command prompt/terminal. 

Next, save the python program with a .py file extension. Open the terminal in the folder where the file is saved and run the program using the command:
python program.py

The python interpreter will execute the instructions in the program. Any output, messages, or results produced by the program will then be displayed in the terminal or console.

If the program requires additional python libraries, install them first using pip, for example:
pip install library_name

After installing the required libraries, run the python file again using the python program.py command.


Repository structure
properties.py: Defines the MaterialProperties dataclass and enforces baseline physical constraints.

material.py: Implements the object-oriented material models and unit conversion properties.

tests.py: Executes mechanical metrics calculations and tracks test history.

utils.py: Provides numeric validation prompts to prevent user input crashes.

database.py: Stores standard material presets and runs the StorageEngine to export results into JSON and CSV files.

main.py: Connects all modules into an interactive console application that runs the analysis loop and triggers file save on exit.






