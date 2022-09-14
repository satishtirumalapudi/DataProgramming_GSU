#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 6.54
##count letters in a string

s=input("Please enter a string :")

def countLetters(p):
    count=0
    temp=[]
    for i in p:
        if (i.isalpha() and i not in temp):
            count=count+1
            temp.append(i)
    return count

print("The count of only unique letters in the given string is ",countLetters(s))
