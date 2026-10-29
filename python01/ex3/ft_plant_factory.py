
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":

    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("SunFlower", 50, 100),
        Plant("Cactus", 10, 90),
        Plant("Oak", 300, 365),
        Plant("Pine", 1000, 5345)
    ]

    for i in plants:
        i.show()