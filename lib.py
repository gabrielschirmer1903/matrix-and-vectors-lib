from random import randint
import operator
import sys
import unittest
import math

#A random point in a 2D space
class Point2D:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init
    
    def distance_to(self, other) -> int:
        res = ((other.x - self.x)**2 + (other.y - self.y)**2 + (other.z - self.z)**2)
        res = math.sqrt(res)
        return res

    def line(p1, p2):
        A = (p1.y - p2.y)
        B = (p2.x - p1.x)
        C = (p1.x*p2.y - p2.x*p2.y)
        return A, B, -C

    def intersection(L1, L2):
        D  = L1[0] * L2[1] - L1[1] * L2[0]
        Dx = L1[2] * L2[1] - L1[1] * L2[2]
        Dy = L1[0] * L2[2] - L1[2] * L2[0]
        if D != 0:
            x = Dx / D
            y = Dy / D
            return x,y
        else:
            return False


class Point3D:
    def __init__(self, x_init, y_init, z_init):
        self.x = x_init
        self.y = y_init
        self.z = z_init
    
    def distance_to(self, other) -> int:
        res = ((other.x - self.x)**2 + (other.y - self.y)**2)
        res = math.sqrt(res)
        return res

#Matrix class 2x2
class Matrix:
    def __init__(self, m, n):
        self.rows = [
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ]
        self.m = m
        self.n = n
    
    def __str__(self) -> str:
        istring=""
        for row in self.rows:
            istring += str(row) + "\n"
        return istring
    
    def __mul__(self, other):
        for x in range(self.m):
            for y in range(self.n):
                print(self.m)
        return other
    def __rmul__(self, other):
        print ('__rmul__')
        return other
    
def random_matrix(m, n) -> Matrix:
    """ Make a random matrix with elements in range (low-high) """
    
    obj = Matrix(m, n)
    for x in range(m):
        for y in range(n):
            obj.rows[x][y] = randint(0, 9)

    return obj