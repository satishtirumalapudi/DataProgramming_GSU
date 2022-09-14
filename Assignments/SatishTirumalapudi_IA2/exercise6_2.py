#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 6.2
##Sum of digits 

x=int(input("Please enter the number: "))
def sumdig(x):
    sum=0
    while(x!=0):
        sum=sum+x%10
        x=x//10
    print("The sum of digits in a given number is",sum)    

sumdig(x)