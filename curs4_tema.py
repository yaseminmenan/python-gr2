import math


class Fractie(object):
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def get_numarator(self):
        return self.numarator

    def set_numarator(self, new_numarator):
        self.numarator = new_numarator

    def get_numitor(self):
        return self.numitor

    def set_numitor(self, new_numitor):
        self.numitor = new_numitor

    def __str__(self):
        return f"Numar: {self.numarator}/{self.numitor}"

    def __add__(self, numar):
        if numar.get_numitor() == self.numitor:
            new_numarator = numar.get_numarator() + self.numarator
            return Fractie(new_numarator, self.numitor)
        else:
            new_numitor = math.lcm(self.numitor, numar.get_numitor())
            new_numarator1 = self.numarator * new_numitor / numar.get_numitor()
            new_numarator2 = numar.get_numarator() * new_numitor / self.numitor
            return Fractie(new_numarator1 + new_numarator2, new_numitor)

    def __sub__(self, numar):
        if numar.get_numitor() == self.numitor:
            new_numarator = self.numarator - numar.get_numarator()
            return Fractie(new_numarator, self.numitor)
        else:
            new_numitor = math.lcm(self.numitor, numar.get_numitor())
            new_numarator1 = self.numarator * new_numitor / numar.get_numitor()
            new_numarator2 = numar.get_numarator() * new_numitor / self.numitor
            return Fractie(new_numarator1 - new_numarator2, new_numitor)

    def inverse(self):
        return Fractie(self.numitor, self.numarator)


num1 = Fractie(5, 2)
print(num1)
num2 = Fractie(1, 2)
num3 = Fractie(1, 3)
print(num2)
print(num3)
print(num1.__add__(num2))
print(num1.__sub__(num2))
print(num2.__add__(num3))
print(num3.__sub__(num2))
print(num1.inverse())
