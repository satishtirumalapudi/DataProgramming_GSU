#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 3.9
######################

##shop1
ws1=int(input("Please enter the weight of rice at shop1 :"))
cost1=int(input("Please enter the cost of packet at shop1 :"))

price1=cost1/ws1
##shop2
ws2=int(input("Please enter the weight of rice at shop2 :"))
cost2=int(input("Please enter the cost of packet at shop2 :"))

price2=cost2/ws2

if price1<price2:
    print("shop1 has better price than shop2")
elif price1>price2:
    print("shop2 has better price than shop1")
else:
    print("Both the shops have a similar price")



