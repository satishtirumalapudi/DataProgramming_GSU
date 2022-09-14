#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 7.31
##Occurrences of each digit in a string

def count(s):
    p = []
    for i in s:
        if i.isdigit():
            
            p.append(int(i))
    print(p)
    countlist = 10 * [0]  #produces a list of size 10

    for element in p:
         # count occurences of number
        if element >= 0 and element <= 9:
            countlist[element] = countlist[element]+1

    for i in range(10):
        if countlist[i] > 0:
            print("count[{}] is ".format(i),countlist[i] )
s=input('Enter the string : ')
count(s)