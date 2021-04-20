import math
a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))

if ((a + b) < c):
    print("Error")
if ((a + c) < b):
    print("Error")
if ((b + c) < a):
    print("Error")
else: 
    s = ((a + b +c) / 2)
    print(float(s))
    area = print(math.sqrt(float(s*(s-a)*(s-b)*(s-c))))    