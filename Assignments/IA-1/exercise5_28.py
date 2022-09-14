#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 5.28
######################
#compute e value 

def evalue(x):
    e=1.0
    d=1
    for i in range(1,x+1):
        d=d*i
        e=e+(1/d)
    return e

for i in range (10000,110000,10000):
    
    print("for value = {} eval is : ".format(i), evalue(i))


    