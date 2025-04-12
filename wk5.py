class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self._power = power           # Encapsulated attribute
        self.level = level

    def introduce(self):
        return f"I am {self.name}, and I possess {self._power}!"

    def fight(self):
        return f"{self.name} fights with {self._power} at level {self.level}."


# Inheritance with specialized class
class Speedster(Superhero):
    def __init__(self, name, level, top_speed):
        super().__init__(name, "super speed", level)
        self.top_speed = top_speed

    def run_fast(self):
        return f"{self.name} runs at {self.top_speed} km/h!"

    # Overriding fight for Speedster
    def fight(self):
        return f"{self.name} blurs past enemies with lightning-fast moves!"

# Example usage:
flash = Speedster("Flash", level=9, top_speed=3500)
print(flash.introduce())
print(flash.run_fast())
print(flash.fight())


#activity 2
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"


# Demonstrating polymorphism
def travel(vehicle):
    print(vehicle.move())


# Example usage:
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    travel(v)
