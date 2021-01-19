from collections import namedtuple

Point1D = namedtuple("Point1D",["x"])
# namedtuple sert a donner des noms aux variables
print(Point1D)

p_04 = Point1D(0.4)
print(p_04)
p_05 = Point1D(0.5)

print(p_04+p_05)

#####
Point2D = namedtuple('Point2D', ['x','y'])

p2d = Point2D(x=0,y=1)
p2d[0]
print(p2d.x)
print(p2d.y)
#####

# Ce qu'on voudrait :
# p_04 + p_05 == Point1D(0.9)
# Ce que l'on a :
# (0.4, 0.5)

def ajout_point(point1, point2):
  x = point1[0] + point2[0]
  print(x)
  return Point1D

print(f"Addition ok:{ajout_point1d(p_04, p_05)}")print(f"Addition ok:{ajout_point1d(p_04, p_05)}")