#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 3.18
######################
#Currency Exchange
usc=float(input("Enter the current exchange rate for 1 usd to chineese Renmibi :"))
cyc=1/usc
print("To convert USD to Chinees Renmibi,please enter 0")
print("To convert Chineese Renmibi to USD,Please enter 1")

conv=int(input("please choose the method "))

if conv==0:
    usd=int(input(("please enter the amount in usd :")))
    print("The amount in Chineese Renmibi is :",usd*usc)
 
elif conv==1:
    cyn=int(input("Please enter the amount in Chineese Renmibi :"))
    print("The amount in USD is :",cyn*cyc)
  
else:
    print("Please enter the correct input for conversion")


