print('Driving theory')
students = int(input("Enter number of students "))
tamrurim = 0
mistakes = 0
i = 0
count = 0
for i in range (students):
    tamrurim = int(input("Enter 'tamrurim' mistakes for this student "))
    mistakes = int(input("Enter all mistakes for student ")) 
    if(tamrurim == 0 and mistakes <= 3):
        count = count + 1
print(count, count/students*100)