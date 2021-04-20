length = int(input('Enter the length of mahrozet in cm '))
radius_of_blue = int(input('Enter the radius in mm '))
radius_of_white = int(input('Enter the radius in mm '))
#Number of blue needed for prepare the mahrozet
print('Only blue', length*10//radius_of_blue)
print('Only white', length*10//radius_of_white)
