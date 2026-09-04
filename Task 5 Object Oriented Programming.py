def get_materials_database() -> Dict[str, Material]:
    steel = MaterialProperties(7850, 250.0, 200.0)
    aluminum = MaterialProperties(2700, 95.0, 69.0)
    titanium = MaterialProperties(4500, 880.0, 114.0)
    polycarbonate_props = MaterialProperties(1200, 62.0, 2.3)
    carbon_fiber_props = MaterialProperties(1600, 600.0, 150.0)

    return {
        "Steel": Metal("Steel", steel, 15.0),
        "Aluminum": Metal("Aluminum", aluminum, 25.0),
        "Titanium": Metal("Titanium", titanium, 10.0),
        "Polycarbonate": Plastic("Polycarbonate", polycarbonate_props),
        "Carbon Fiber": Composite("Carbon Fiber", carbon_fiber_props, "3K Carbon")
    }


def get_material(name: str, database: Dict[str, Material]) -> Optional[Material]:
    db_lookup = {key.lower(): key for key in database}
    cleaned_name = name.strip().lower()

    if cleaned_name in db_lookup:
        return database[db_lookup[cleaned_name]]

    return None