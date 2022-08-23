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

    def __str__(self) -> str:
        return('x: ' + str(self.x) + '    y: ' + str(self.y))
    
    def distance_to(self, other) -> int:
        res = ((other.x - self.x)**2 + (other.y - self.y)**2 + (other.z - self.z)**2)
        res = math.sqrt(res)
        return res

    def line(p1, p2):
        A = (p1.y - p2.y)
        B = (p2.x - p1.x)
        C = ((p1.x * p2.y) - (p2.x * p1.y))
        return A, B, -C

    def intersection(L1, L2):
        Det  = (L1[0] * L2[1]) - (L1[1] * L2[0])
        DetX = (L1[2] * L2[1]) - (L1[1] * L2[2])
        DetY = (L1[0] * L2[2]) - (L1[2] * L2[0])
        if Det != 0:
            x = DetX / Det
            y = DetY / Det
            return x,y
        else:
            return False


class Point3D:
    def __init__(self, x_init, y_init, z_init):
        self.x = x_init
        self.y = y_init
        self.z = z_init
    def __str__(self) -> str:
        return('x: ' + str(self.x) + '    y: ' + str(self.y) + '    z: ' + str(self.z))
    
    def distance_to(self, other) -> int:
        res = ((other.x - self.x)**2 + (other.y - self.y)**2)
        res = math.sqrt(res)
        return res

#Matrix class 2x2
class Matrix:
    def __init__(self, m, n):
        match m:
            case 4:
                self.rows = [
                    [1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]
                ]
            case 3:
                self.rows = [
                    [1,0,0],[0,1,0],[0,0,1]
                ]
            case 2:
                self.rows = [
                    [1,0],[0,1]
                ]
            case 1:
                self.rows = [
                    [1]
                ]
            case _:
                return false
        self.m = m
        self.n = n
    
    def __str__(self) -> str:
        istring=""
        for row in self.rows:
            istring += str(row) + "\n"
        return istring
    
    def __mul__(self, other):
        res = Matrix(self.m, self.n)

        for x in range(self.m):
            for y in range(self.n):
                res.rows[x][y] = 0
                for z in range(self.m):
                    res.rows[x][y] += self.rows[x][z] * other.rows[y][z]
        return res

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