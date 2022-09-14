#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 4.4

######################

#Geometry: area of a hexagon

import math

s=int(input("Enter the length of a side :"))

area=(6*math.pow(s,2))/(4*math.tan((math.pi)/6))

print("The area of the heaxagon is ",area)
