#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 2.11
######################
import math

FAV=int(input("Please enter the final account value :"))
AIR=float(input("Please enter the annual interest rate: "))
##converting the annual interest percentage into value
AIRI=AIR/100
#to convert annual interest to monthly interest divide it by 12
MIR=AIRI/12

years=int(input("Please enter the years"))
#to convert years into months multiply it by 12 
months=years*12

ida=FAV/(1+MIR)**months

print("The initial deposit amount is",ida)
