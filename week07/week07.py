from enum import IntEnum
from abc import ABC


class Animal(ABC):

    class BodyShape(IntEnum):
        SMALL = 1
        MID = 2
        BIG = 3

    def __init__(self, kind, body, character):
        self.kind = kind
        self.body = self.BodyShape(body)
        self.character = character

    @property
    def isFerocity(self):
        if self.body >= self.BodyShape.MID and self.kind == 'predator' \
            and self.character == 'violent':
            return True
        return False
        


class Zoo(object):
    
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)

class Cat(Animal):
    bark = 'Meow'

    def __init__(self, name, kind, body, character):
        self.name = name
        super().__init__(kind, body, character)

    @property
    def isPet(self):
        return False if self.isFerocity else True


class Dog(Animal):
    bark = 'Wow'

    def __init__(self, name, kind, body, character):
        self.name = name
        super().__init__(kind, body, character)

    @property
    def isPet(self):
        return False if self.isFerocity else True

