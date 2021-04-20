import math
print("Enter equation numbers a,b,c")
print("ax^2 + bx +c = 0")
a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))

discr = b ** 2 - 4 * a * c
print("Discriminant D = %.2f" % discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("No roots")

#print(-b(math.sqrt(b**2-4*a*c))/(2*a))