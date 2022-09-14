#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 8.41
##Sort students

number = int(input('enter the number of students'))
list1 = []
for i in range(0,number):
    score,name = input('enter student score and name').split()
    list1.append((score,name))


list1 = sorted(list1)

print('Score \t student')
for i in list1:
    print(i[1],"\t",i[0])