#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 1.7
######################
#value of pi is calculated here
sum=0
p=0
den=int(input("Please enter the denominator"))
for i in range (1,den+2,2):
    p=p+1
    if p%2!=0:
        sum+=(1/i)
    else:
        sum-=(1/i)
print("The pi value for denominator entered is =",sum*4)


