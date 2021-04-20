x = str(input('Enter the number of Letters that you want to get'))
y = ord(x)
b = 0
while y!=123:
     print('The next letter is', chr(y))   
     y = y + 1
     if y == 123:
        print('we goin to start')
        y = 97
        b = b + 1  
     if b == 2:
         break