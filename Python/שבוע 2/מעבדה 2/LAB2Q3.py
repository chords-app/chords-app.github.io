m = int(input("Enter month"))
s = float(input("Enter sallary"))
#AVG OF DAY SALLARY
if (m == 2):
    d = 28 - 8
if (m == (4 or 6 or 9 or 11)):
    d = 30 - 8
else: 
    d = 31 - 8
print(("AVG OF SALLARY OF DAY IN THIS MONTH", s/d ))