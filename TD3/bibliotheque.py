from collections import namedtuple

Point1D = namedtuple("Point1D", ["x"])
Point2D = namedtuple("Point2D", "x y")

def ajout_point1d(point1, point2):
  x = point1.x + point2.x
  return Point1D(x)

  
def norme1d(p1):
    return (p1.x ** 2) ** 0.5 

assert True