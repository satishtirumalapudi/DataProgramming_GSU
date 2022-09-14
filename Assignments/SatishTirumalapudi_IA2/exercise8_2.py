#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 8.2
##Sum the major diagonal in a matrix

def sumMajorDiagonal(m):
    sum=0
    for i in range(0,len(m)):
        j=i
        sum = sum + m[i][j]
    return sum;

#To comnpute the diagonal sum of matrix row and column should be equal
rowcoulm=int(input("Enter the number of row/column :"))
mat = [[int(input()) for x in range (rowcoulm)] for y in range(rowcoulm)]
print(mat)
print('sum of diagnol elements of given matrix is ', sumMajorDiagonal(mat))