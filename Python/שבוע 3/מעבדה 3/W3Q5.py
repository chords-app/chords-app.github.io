a = str(input('Enter first letter '))
b = str(input('Enter second letter '))
c = str(input('Enter third letter '))



if (ord(a)+1) == ord(b) and (ord(b)+1 == ord(c)):
    x = ord(c) + 1
    print(chr(x))
else:
    print('it is a not growing system of chars')
