num = int(input("Enter two digit number"))
l = 0
r = 0
max = 0
maxnum = 0
l1 = 0
r1 = 0 
flag = 1
count = 0 
while (flag == 1):
     if ((l%2==0 and r%2==1) or (l%2==1 and r%2==0)):
          flag = 0
          l1 = l
          r1 = r
          print ( l , r )
          if ((l1 + r1) > max ):
               max = r1 + l1
               maxnum = num
     else:
         num = int(input("Enter two digit number")) 
         count = count + 1
         l = num//10
         r = num%10
         l1 = l 
         r1 = r
         if ((l1 + r1) > max ):
               max = r1 + l1
               maxnum = num
print(maxnum, max, count)