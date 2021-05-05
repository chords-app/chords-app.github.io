y = int(input("Enter the today year please "))  
i = 1  
c = 1   
s = 0 
sh = 0
h = 0
while(c > 0):
    c = int(input("Enter the year of birth of child "))
    print(i)
   # a = y - c
   # print(a)
    if (y-c > 15 and y-c < 18):
        i = i + 1
        if(y - c == 16):
           s = s + 1
        if(y - c == 17):
           sh = sh + 1
        if(y - c == 15):
           h = h + 1
        if (i > 5):
            print('You can make the school')
            print(s,sh,h)
        else:
            print('You can\'t make the school') 
        