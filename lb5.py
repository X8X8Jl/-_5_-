from abc import ABC, abstractmethod
# Абстрактний клас Species
class Species(ABC):
    def init(self, name):  # Замість init повинен бути init
        self.name = name

        @abstractmethod
        def interact(self, other):
            pass