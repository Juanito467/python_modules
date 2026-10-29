

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self, height: int) -> None:
        if height > 0:
            self._height += height

    def age(self, age: int) -> None:
        if age > 0:
            self._age += age


class Flower(Plant):
    def __init__(self, name, height, age, color: str) -> None:
        super().__init__(name, height, age) 
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        if self.bloomed is False:
            print("[asking the flower to bloom]")
            self.bloomed = True
        else:
            print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed is False:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the tree to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self._height}cm"
            f" long and {self.trunk_diameter}cm wide."
            )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def set_height(self, height) -> None:
        super().set_height(height)
        self.nutritional_value += 10

    def set_age(self, age) -> None:
        super().set_age(age)
        self.nutritional_value += 10


def  main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    flower.bloom()
    flower.show()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    tree.produce_shade()
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    vegetable.show()
    vegetable.age(20)
    vegetable.grow(42)
    vegetable.show()


if __name__ == "__main__":
    main()
