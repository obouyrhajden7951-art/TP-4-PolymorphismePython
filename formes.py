from abc import ABC, abstractmethod
import math


class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} – aire : {self.aire():.2f}"


class Cercle(Forme):
    def __init__(self, r):
        self.r = r

    def aire(self):
        return math.pi * self.r ** 2


class Rectangle(Forme):
    def __init__(self, larg, haut):
        self.larg = larg
        self.haut = haut

    def aire(self):
        return self.larg * self.haut


class Triangle(Forme):
    def __init__(self, base_tri, haut):
        self.base_tri = base_tri
        self.haut = haut

    def aire(self):
        return 0.5 * self.base_tri * self.haut


if __name__ == "__main__":
    liste_formes = [
        Cercle(3),
        Rectangle(4, 5),
        Triangle(6, 2)
    ]

    for forme in liste_formes:
        print(forme)