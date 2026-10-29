class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def ft_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def ft_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def both_errors() -> None:
    try:
        ft_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        ft_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        ft_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        ft_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    both_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()