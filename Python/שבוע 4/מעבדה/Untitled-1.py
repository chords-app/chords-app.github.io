num = int(input("Enter a number :"))
r=num%10
l=num//10
max=r+l
flag=True
if(r%2==0 and l%2==0)or(r%2==1 and l%2==1):
    while(flag):
        num = int(input("Enter a number :"))
        r=num%10
        l=num//10
        if(r+l>max):
            max=r+l
        if!(r%2==0 and l%2==0)or(r%2==1 and l%2==1): 
           flag=False