

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

        self.stats = self.Stats()

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        self.stats.set_show_count()

    def grow(self, height: int) -> None:
        if height > 0:
            self._height += height
            self.stats.set_grow_count()

    def age(self, age: int) -> None:
        if age > 0:
            self._age += age
            self.stats.set_age_count()

    @staticmethod
    def older_tester(age: int) -> None:
        return age > 365

    @classmethod
    def anonymous_plant(cls):
        name = "Unknown Plant"
        return cls(name, 0.0, 0)

    class Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def set_grow_count(self):
            self._grow_count += 1

        def set_age_count(self):
            self._age_count += 1

        def set_show_count(self):
            self._show_count += 1

        def display_stats(self):
            print(
                f"Stats: {self._grow_count} grow, {self._age_count} age"
                f", {self._show_count} show"
                )

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
        self.shade = 0

    def produce_shade(self) -> None:
        print("[asking the tree to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self._height}cm"
            f" long and {self.trunk_diameter}cm wide."
            )
        self.shade += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def display_shade(self) -> None:
        print(f" {self.shade} shade")


class Seed(Flower):
    def __init__(self, name, height, age, color, seed: int):
        super().__init__(name, height, age, color)
        self.seed = seed

    def show(self):
        super().show()
        print(f" Seeds: {self.seed}")

    def bloom(self) -> None:
        super().bloom()
        self.seed = 42


def  main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Check year-old")
    print(f"Is 30 older than a year? -> {Plant.older_tester(30)}")
    print(f"Is 400 older than a year? -> {Plant.older_tester(400)}")
    print("\n=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    print(f"[statistics for {flower.name}]")
    flower.stats.display_stats()
    flower.bloom()
    flower.show()
    print(f"[statistics for {flower.name}]")
    flower.stats.display_stats()
    print("\n=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print(f"[statistics for {tree.name}]")
    tree.stats.display_stats()
    tree.display_shade()
    tree.produce_shade()
    tree.stats.display_stats()
    print("\n=== Seed")
    seed = Seed("SunFlower", 80.0, 45, "yellow", 0)
    seed.show()
    seed.bloom()
    seed.age(20)
    seed.grow(40.0)
    seed.show()
    print(f"[statistics for {seed.name}]")
    seed.stats.display_stats()
    print("\n=== Anonymous")
    anonymous = Plant.anonymous_plant()
    anonymous.show()
    print(f"[statistics for {anonymous.name}]")
    anonymous.stats.display_stats()


if __name__ == "__main__":
    main()
