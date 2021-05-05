def func1(a):
    count = 0
    while (a!=0):
       
        b = a%10
        a = a//10
        if (b%2==0):
            count = count + 1
    return count

n = int(input('Enter the count of numbers that you want to check '))
max_digits = 0
for i in range (0,n,1):
    print(i)
    a = int(input('Enter number bigger than 0 '))
    while(a < 0):
        a = int(input('Enter number bigger than 0 '))
    
    d = func1(a) 
    print("The even digits' in this number is " , d)
    if (d > max_digits):
        max_digits = d
        c = a

print("The maximum even digits is", max_digits, "the number is ", c)
        

