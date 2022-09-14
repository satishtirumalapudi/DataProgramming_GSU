#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 7.13
##Eliminate Duplicates

list1= [int(num) for num in input("Please enter the elements in the list :\n").split(" ")]

def eliminateDuplicates(lst):
    l=set(lst)
    print("The unique elements in the list are :",l)

eliminateDuplicates(list1)