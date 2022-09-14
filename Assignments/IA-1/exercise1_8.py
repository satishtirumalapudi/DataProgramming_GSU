#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 1.8
######################
sum=0
p=1
for i in range (1000):
    if i%2==0:
        sum=sum+(1/p)
    else:
        sum=sum-(1/p)
    p=p+2
 
pi=sum*4
radius=5.5
area=pi*radius*radius
perimeter=2*pi*radius
print("The perimeter of the circle is",perimeter)
print("The area of the circle is ",area)
