# print("Curs 4 - OOP")

class Coordinate(object):
    """ O coordonata este compusa din valorile x si y """

    def __init__(self, x, y):
        """ Setam valorile lui x s y """
        self.x = x
        self.y = y

    def __str__(self):
        """ Afisam coordonatele x si y """
        return f"<{self.x}, {self.y}>"

    def distance(self, other):
        """ Returnam distanta euclidiana dintre doua coordonate"""
        x_diff_square = (self.x - other.x) ** 2
        y_diff_square = (self.y - other.y) ** 2
        return (x_diff_square + y_diff_square) ** 0.5


origin = Coordinate(0, 0)
print(origin)
print(origin.x)
print(origin.y)

c1 = Coordinate(0, 1)
c2 = Coordinate(10, 20)

print(c1)
print(c2)

print(c1.distance(c2))
print(origin.distance(c1))


