import math

def d(a, b, c):
    return b**2 - 4*a*c

def x1_x2(a, b, c):
    discriminant = d(a, b, c)
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"Single root: {root}")
    else:
        print("No real roots")
