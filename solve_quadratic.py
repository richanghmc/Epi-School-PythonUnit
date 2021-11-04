import math
def solve_quadratic(a,b,c):
    if (b*b - 4*a*c) < 0:
        return None
    root1 = (-b + math.sqrt(b*b - 4*a*c))/ (2*a)
    root2 = (-b - math.sqrt(b*b - 4*a*c))/ (2*a)
    if root1 == root2:
        return root1
    return (root1,root2)