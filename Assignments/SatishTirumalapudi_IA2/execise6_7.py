#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 6.7
##Future investement value

investmentAmount=int(input("Please enter the investment amount :"))
years= int(input("Enter the number of years :"))
annualInterestRate=int(input("Please enter the annual interest rate in percentage :"))
annualint=annualInterestRate/(100)



def futureInvestmentValue(investmentAmount,annualint,years):
    for i in range(1,years+1):
        futureInvestmentValue=0
        futureInvestmentValue=investmentAmount*(1+annualint/12)**(i*12)
        print("The future investment value is",futureInvestmentValue,"for",i,"year")

futureInvestmentValue(investmentAmount,annualint,years)