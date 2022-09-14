#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 5.39
######################
#Financial application: find the sales amount

#Base salary is given as 5000$
basesal=5000
#The Required commision is 30000$
commreq=30000
#More minsales required would be commision miunus base salary we already have
commearn=30000-5000
#Commision for first 5 thousand is 8%
comm1=basesal*8/100
#commision for next 5 thousand is 10%
comm2=basesal*10/100
#Required commision to meet the expected minsales is 
commearn=commearn-(comm1+comm2)

#Minimum sales we have to do meet the required commision 
#We have to add basesalary of 10,000 as the commision required to earn is greater than 10,000
minsal=10000+((commearn*100)/12)

print("The Minimum sales required for the required commission of 30,000$ is ",minsal)




