#Task 4 Functions and Parameters

def create_calculation_record(material, inputs, results):
    """Creates a dictionary containing the calculation information."""
    record = {
        "material": material,
        "force": inputs["force"],
        "area": inputs["area"],
        "original_length": inputs["original_length"],
        "change_in_length": inputs["change_in_length"],
        "stress_pa": results["stress_pa"],
        "stress_mpa": results["stress_mpa"],
        "strain": results["strain"],
        "calc_modulus_gpa": results["calc_modulus_gpa"],
        "safety_factor": results["safety_factor"],
        "safety_status": results["safety_status"]
    }
    return record


def add_to_history(history_list, record):
    """Adds a calculation record to the calculation history."""
    history_list.append(record)