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

class ResourceCycle:
    def init(self, resources):
        self.resources = resources

    def cycle_resources(self):
        print(f"Resources are being cycled: {self.resources}")
# Ключові методи
def introduce_species(species_list, new_species):
    species_list.append(new_species)
    print(f"{new_species.name} introduced to the ecosystem.")

def simulate_interactions(species_list):
    for i in range(len(species_list)):
        for j in range(i + 1, len(species_list)):
            Interaction(species_list[i], species_list[j]).simulate()

def adjust_climate(climate, temp_change, humidity_change):
    climate.adjust_climate(temp_change, humidity_change)

def monitor_biodiversity(species_list):
    print("Current biodiversity in the ecosystem:")
    for species in species_list:
        print(f"- {species.name}")
def balance_ecosystem(resource_cycle):
    resource_cycle.cycle_resources()
    print("The ecosystem is balanced.")

species_list = []
introduce_species(species_list, Plant("Oak Tree"))
introduce_species(species_list, Animal("Deer"))
introduce_species(species_list, Microorganism("Bacteria"))

climate = Climate(25, 70)

