#while (a>=10 and a<=99):
a = int(input('Enter 1 number'))
#while (b>=10 and b<=99):   
b = int(input('Enter 2 number'))


c = a%10 
print('c',c)     
a = a//10
print('a',a) 

d = b%10
print('d',d)
b = b//10
print('b',b)



if (c == d or c == b) and (a == b or a == d):
    print('Yes they maded from the same numbers')
else:
    print('No they not maded from the same numbers')
    
