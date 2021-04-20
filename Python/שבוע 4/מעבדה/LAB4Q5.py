
cou = 0
flag = 0
a = int(input(' Enter a two digit number'))
while (a>=10 or a<=99 and flag == 1):
   b = a//10
   c = a%10
   if (b%2==0 and c%2!=0):
       flag = 1
       #print('zugi no zugi' )
   elif (b%2!=0 and c%2==0):
       flag = 1
       #print('izugi zugi')    
   else:
       g = a 
       print ('zugi zugi or izugi izugi')
       cou += 1
       a = int(input(' Enter a two digit number'))
print(cou)
