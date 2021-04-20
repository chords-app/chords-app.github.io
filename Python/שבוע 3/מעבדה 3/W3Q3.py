a = int(input('Input a number '))
b = int(input('Input b number '))
c = int(input('Input c number '))

if a < b and b < c:
    print('This growing serial of numbers')
    print(b-a)
    print(c-b)
else: 
    print('This is not growing serial of numbers')