
def func1(a):
    sum = 0
    while (a!=0):
        b = a%10
        a = a//10
        sum = sum + b
        print("The righ digit ",b)
        print("Sum is  ", sum)
    return sum

def func2 (sum):
    flag = 0
    if (sum % 3 == 0):
        flag = 1
    return flag
        

a = int(input("Enter some number "))
while (a < 0):
    a = int(input("Enter some number "))

sum = func1(a)
if(func2(sum) == 1):
    print('This number is can be divided by 3 ')
