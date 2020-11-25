
from math import sqrt, pi
A = int(input("Enter 1st number"))
B = int(input("Enter 2nd number"))
C = int(input("Enter 3rd number"))
D = int(input("Enter 4th number"))

X = A + B + C + D
print("Total = ", X)
R = sqrt(X/pi)
print("Radius = ", R)

A1 = (360/X) * A
B1 = (360/X) * B
C1 = (360/X) * C
D1 = (360/X) * D
print(A1,   B1,    C1,    D1)
print("Thank You ")
