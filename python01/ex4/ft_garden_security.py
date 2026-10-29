

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def set_age(self, age: int) -> int:
        if age > 0:
            print(f"Age updated: {age} days")
            self._age = age
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def set_height(self, height: float):
        if height > 0:
            print(f"Heigh updated: {height} days")
            self._height = height
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def get_age(self):
        return self._age

    def get_height(self):
        return self._height


def status(plant: Plant) -> None:
    print(f"Current state: {plant.name}: {plant.get_height()}cm, {plant.get_age()} days old")


def     main() -> None:
    print("=== Garden Security System ===")
    p1 = Plant("Rose", 15.0, 10)
    print(f"Plant created: {p1.name} : {p1.get_height()}cm, {p1.get_age()} days old")
    print("\n")
    p1.set_height(25.0)
    p1.set_age(30)
    print("\n")
    p1.set_height(-10)
    p1.set_age(-12)
    print("\n")
    status(p1)


if __name__ == "__main__":
    main()