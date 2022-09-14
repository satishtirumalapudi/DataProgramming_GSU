#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 7.8
##Index of smallest element

lst= [int(num) for num in input("Please enter the elements in the list :\n").split(" ")]
def indexOfSmallestElement(k):
    min1=min(k)
    for j in range(len(k)):
        if k[j]==min1:
            print("The index of Minimum element in the list :",j)
            break

indexOfSmallestElement(lst)