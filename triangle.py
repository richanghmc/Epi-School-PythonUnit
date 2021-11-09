from math import *

class Triangle():
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        semiPerimeter = (self.a + self.b + self.c)/2
        return sqrt(semiPerimeter * (semiPerimeter - self.a) * (semiPerimeter - self.b) * (semiPerimeter - self.c))
    
    def is_valid(self):
        if self.a + self.b <= self.c or self.b + self.c <= self.a or self.a + self.c <= self.b:
            return False
        return True

    def is_right(self):
        if self.a**2 + self.b**2 == self.c**2 or self.a**2 + self.c**2 == self.b**2 or self.b**2 + self.c**2 == self.a**2:
            return True
        return False
