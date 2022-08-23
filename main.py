from lib import *

p1 = Point2D(1,1)
p2 = Point2D(5,5)
p3 = Point2D(1,3)
p4 = Point2D(3,1)

L1 = Point2D.line(p1, p2)

L2 = Point2D.line(p3, p4)

aa = Point2D.intersection(L1, L2)

print (aa)


