def prompt_positive_float(prompt_text: str) -> float:
    while True:
        try:
            value = float(input(prompt_text))
            if value <= 0:
                print("  [Error]: Value must be greater than zero.")
                continue
            return value
        except ValueError:
            print("  [Error]: Invalid numerical input. Try again.")


def prompt_non_zero_float(prompt_text: str) -> float:
    while True:
        try:
            value = float(input(prompt_text))
            if value == 0:
                print("  [Error]: Value cannot be zero.")
                continue
            return value
        except ValueError:
            print("  [Error]: Invalid numerical input. Try again.")