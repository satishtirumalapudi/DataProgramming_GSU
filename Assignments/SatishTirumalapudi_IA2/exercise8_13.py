#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 8.13
##Maximum element is obtained at position 
def locatelargest(matrix):

    max = -1
    
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if max < matrix[i][j]:
                max = matrix[i][j]
                rowPos = i
                colPos = j

    return [rowPos,colPos]

rows=int(input("Enter the number of rows :"))
columns = int(input("Enter the number of coulumns :"))
mat = [[int(input()) for x in range (rows)] for y in range(columns)]
print(mat)
print("Maximum element is found at postion: ",end="")
print(str(locatelargest(mat)))

