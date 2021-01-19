from collections import namedtuple

Point1D = namedtuple("Point1D",["x"])
# namedtuple sert a donner des noms aux variables
print(Point1D)

p_04 = Point1D(0.4)
print(p_04)
p_05 = Point1D(0.5)

print(p_04+p_05)

# Ce qu'on voudrait :
# p_04 + p_05 == Point1D(0.9)
# Ce que l'on a :
# (0.4, 0.5)

def ajout_point1d(point1, point2):
  x = point1.x + point2.x
  
  return Point1D(x)

print(f"Addition ok:{ajout_point1d(p_04, p_05)}")

def norme1d(p1):
  return (p1.x**2) ** 0.5

p_09 = ajout_point1d(p_04, p_05)

print(norme1d(p_09))


#####

Point2D = namedtuple('Point2D', ['x','y'])

p2d = Point2D(x=0,y=1)
p2d[0]
print(p2d.x)
print(p2d.y)

p1 = Point2D(0, 1) 
p2 = Point2D(1, 0)
print(p1)
print(p2)
print("*************")

def ajout_point2d(p_1, p_2):
  x = p_1[0] + p_2[0]
  y = p_1[1] + p_2[1]
  return Point2D(x, y)

p3 = ajout_point2d(p1,p2)
print(p3)

print(f"Addition ok: {ajout_point2d(p1, p2) == Point2D(1,1)}")




