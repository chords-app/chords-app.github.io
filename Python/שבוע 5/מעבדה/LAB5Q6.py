""""print('Perfect number ')
i = 1
j = 1
sum = 0
count = 0
for i in range (1000):
    for j in range (i):
        if (i//j==0):
            sum = i%j + sum
            if (sum == i):
                count = count + 1 
print(count)
"""

# Python Program to find Perfect Number using For loop

Number = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print(" %d is a Perfect Number" %Number)
else:
    print(" %d is not a Perfect Number" %Number)