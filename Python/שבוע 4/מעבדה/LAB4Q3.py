x = 0 #Ask anout filtering for 3 digits number
while (x!=7):
      a = int(input('Enter 3 digit number')) 
      a1 = a%10 
      #print(a1) 
      a2 = a//10 
      a3 = a2%10
      #print(a3)
      a4 = a2//10 
      #print(a4)
      x = x + 1
      #my numbers is a1, a3, a4
      if(a1 == a2 or a1 == a3 or a2 == a4):
           print('This number have same digits') 
      else:
           print(a)      
    


