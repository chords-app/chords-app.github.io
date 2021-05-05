
num = int(input("Enter a number please bigger then 0 "))
i = 0
x = 0
a = num//2
while ( num < 0):
    num = int(input("Enter a number please bigger then 0 "))
for i in range (0, num):
    if(i%2==1):
        print(i)
        x = x+1
print("For the current input, The loop will be performed: ", a , " times ")
print ("For checking lets see ", x)
