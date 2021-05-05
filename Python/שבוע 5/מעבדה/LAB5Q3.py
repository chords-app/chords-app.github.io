#print("Enter the degre of the middle period and end of the year")
a = 0
b = 0
i = 0
s = int(input("Enter the number of students"))
for i in range (s) :
    print('Enter the degrees of student number ', i+1)
    a = float(input("Enter the middle period degre of student "))
    a1 = a//10
    a2 = a - a1
    while(a < 40 or a > 100):
        a = float(input("Enter the middle period degre "))
        a1 = a//10
        a2 = a - a1
    b = float(input("Enter the overall period degre"))
    b1 = b//10
    b2 = b - b1
    while(b < 40 or b > 100):
        b = float(input("Enter the overall period degre"))
        b1 = b//10
        b2 = b - b1
    print(a1, a2, b1, b2)
    
