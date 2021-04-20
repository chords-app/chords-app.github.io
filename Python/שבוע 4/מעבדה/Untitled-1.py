
while (a<=10 or a>=99 and (a)):
   a = int(input(' Enter a two digit number'))
   b = a//10
   c = a%10
   if (b%2==0 and c%2!=0):
       break
       #print('zugi no zugi' )
   elif (b%2!=0 and c%2==0):
       break
       #print('izugi zugi')    
   else:
      print ('zugi zugi or izugi izugi')

      cou += 1