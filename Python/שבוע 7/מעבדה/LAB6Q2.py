import math
def func1(a):
    if(a>0):
        b = math.floor(a)
    if (a<0):
        b = math.ceil(a)
    return b


a = float(input("Enter some number "))
print(a)

d = func1(a)
print(d)