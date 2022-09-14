#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 7.7 
##Random number Generator(1-10 and count)
import random
list1=[]
list2=[]
for i in range(0,1000):

    ra=random.randint(0,9)
    list1.append(ra)
for j in range(0,10):
    a=list1.count(j)
    list2.append(a)

for k in range (0,10):
    print("Number of times ",k,"repeated are :",list2[k])
