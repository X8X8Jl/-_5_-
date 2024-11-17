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
