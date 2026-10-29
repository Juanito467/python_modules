class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Invalid plant name to water"):
        super().__init__(message)


def water_plant(plant_name: str):
    temp = plant_name.capitalize()
    if plant_name == temp:
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: {plant_name}")


def test_watering_system():
    print("Testing valid plants...")
    plants = ["Tomate", "Lettuce", "Carrots"]
    try:
        print("Opening watering system")
        for i in plants:
            water_plant(i)
    except PlantError as e:
        print(f"Caugh PlantError: {e}")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    plantsfail = ["Tomate", "lettuce", "Carrots"]
    try:
        print("Opening watering system")
        for i in plantsfail:
            water_plant(i)
    except PlantError as e1:
        print(f"Caught PlantError: {e1}")
        print(".. ending test and returning to main")
        return
    finally:
        print("Closing watering system")


def main():
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with erros!")


if __name__ == "__main__":

    main()
