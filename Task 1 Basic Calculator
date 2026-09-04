# Part 1: Basic Stress and Strain Calculator Template

def main():
    """Main function for the stress and strain calculator."""

    print("=== Stress and Strain Calculator ===\n")
    force = float(input("Enter applied force: "))
    area = float(input("Enter cross-sectional area: "))
    original_length = float(input("Enter original length: "))
    change_in_length = float(input("Enter change in length: "))

    #Formulas for Stress, Strain, Stress in MPa, and Loading
    stress = force / area
    strain = change_in_length / original_length

    stress_mpa = stress / 1000000

    if stress_mpa > 0:
      loading = "Tension"
    else:
      loading = "Compression"

    #Print out the results with the proper format
    print("\n=== RESULTS ===\n")
    print(f"Stress: {stress:.2f} Pa")
    print(f"Strain: {strain:.6f}")
    print(f"Stress (MPa): {stress_mpa:.2f}")
    print(f"Loading: {loading}")
    print("\n=== Analysis Complete ===")

if __name__ == "__main__":
    main()