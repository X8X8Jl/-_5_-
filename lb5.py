from abc import ABC, abstractmethod
# Абстрактний клас Species
class Species(ABC):
    def init(self, name):  # Замість init повинен бути init
        self.name = name

    @abstractmethod
    def interact(self, other):
        pass

# Підкласи для видів рослин, тварин і мікроорганізмів
class Plant(Species):
    def interact(self, other):
        print(f"{self.name} provides oxygen to {other.name}.")

class Animal(Species):
    def interact(self, other):
        if isinstance(other, Plant):
            print(f"{self.name} eats {other.name}.")
        elif isinstance(other, Animal):
            print(f"{self.name} interacts with {other.name} (e.g., predator-prey).")
class Microorganism(Species):
    def interact(self, other):
        print(f"{self.name} breaks down organic material for {other.name}.")
# Клас Environment
class Environment:
    def init(self, type):  # Замість init повинен бути init
        self.type = type

class Climate:
    def init(self, temperature, humidity):  # Замість init повинен бути init
        self.temperature = temperature
        self.humidity = humidity

    def adjust_climate(self, temp_change, humidity_change):
        self.temperature += temp_change
        self.humidity += humidity_change
        print(f"Climate adjusted: Temperature={self.temperature}, Humidity={self.humidity}")

# Клас Interaction
class Interaction:
    def init(self, species1, species2):  # Замість init повинен бути init
        self.species1 = species1
        self.species2 = species2

    def simulate(self):
        self.species1.interact(self.species2)
