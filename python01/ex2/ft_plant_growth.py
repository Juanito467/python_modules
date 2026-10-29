
class Plant:
    def __init__(self, name: str, height: float, age_days: int, growth: float) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth = growth

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.age_days += 1

if __name__ == "__main__":

    plant_1 = Plant("Rose", 25.0, 30, 0.8)
    initial_height = plant_1.height

    print("=== Garden Plant Growth ===")
    print(f"{plant_1.name}: {plant_1.height}cm, {plant_1.age_days} days old")
    for i in range(1, 8):
        plant_1.grow()
        plant_1.age()
        print(f"=== Day {i} ===")
        print(f"{plant_1.name}: {plant_1.height:.1f}cm, {plant_1.age_days} days old")
    print(f"Growth this week: {plant_1.height - initial_height:.1f}cm")
