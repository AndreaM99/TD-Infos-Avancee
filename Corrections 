from collections import namedtuple


Point1D = namedtuple("Point1D", ["x"])


p_04 = Point1D(0.4)
p_05 = Point1D(0.5)

print(p_04 + p_05)


def ajout_point1d(p_1, p_2):
    return Point1D(p_1.x + p_2.x)


p_09 = ajout_point1d(p_04, p_05)

print("point 09 ok ?", p_09 == Point1D(0.9))


def norme1d(p1):
    return (p1.x ** 2) ** 0.5


print(norme1d(p_09))

Point2D = namedtuple("Point2D", "x y")

p1 = Point2D(0, 1)
p2 = Point2D(1, 0)

print(p1)
print(p2)

p3 = p1 + p2

print(p3)


def ajout_point2d(p_1, p_2):
    x = p_1[0] + p_2[0]
    y = p_1[1] + p_2[1]
    return Point2D(x, y)


p3 = ajout_point2d(p1, p2)
print(p3)


def ajout_point2d(p_1, p_2):
    coord = []
    for indice in range((len(p_1))):
        coord.append(p_1[indice] + p_2[indice])
    return Point2D(coord[0], coord[1])


p4 = ajout_point2d(p1, p2)
print(p4)

print("False:", p3 == (0, 1))
print(p3 == (1, 1))
print(p3 == (1, 1))


def ajout_point2d(p_1, p_2):
    coord = tuple(x + y for x, y in zip(p_1, p2))
    return Point2D(coord[0], coord[1])


p5 = ajout_point2d(p1, p2)


print(p3 == p4 == p5 == (1, 1))


def ajout_point2d(p_1, p_2):
    coord = tuple(x + y for x, y in zip(p_1, p2))
    return Point2D._make(coord)


p6 = ajout_point2d(p1, p2)


print(p6 == p5)


class Point1D:
    def __init__(self, x):
        self.x = x


np1d = Point1D(0.9)

print(norme1d(np1d))

# Afficher un point


def afficher_point1d(point):
    print(f"Point: {point.x}")


afficher_point1d(np1d)

print(np1d)
np1d_2 = Point1D(0.9)
print(np1d_2)


class Point1D:
    def __init__(self, x):
        self.x = x

    def affiche(self):
        return f"{self.x}"


np1d = Point1D(0.9)

print(np1d.affiche())
