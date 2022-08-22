from random import randint
import operator
import sys
import unittest

#A random point in a 2D space
class Point2D:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init
    
    def distance_to(self, other) -> int:
        print("calculate distance between " + self + " " + other)

class Point3D:
    def __init__(self, x_init, y_init, z_init):
        self.x = x_init
        self.y = y_init
        self.z = z_init

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