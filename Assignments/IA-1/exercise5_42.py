#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 5.42

##Process string
######################
s1=input("Enter a string :")

length=len(s1)
even=""
odd=""
for i in range(length):
    if i%2== 0:
        even=even+s1[i]
    else:
        odd=odd+s1[i]
print("The characters at odd position are :",odd)
