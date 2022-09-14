#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 6.52
##Longest common prefix

def commprefix(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    i = 0
    j = 0
    ans=""
    while i <= len1 - 1 and j <= len2 - 1:
     
        if (s1[i] != s2[j]):
            break
             
        ans += s1[i]
        i += 1
        j += 1
 
    return (ans)

string1=input("Please enter the first string :")
string2=input("Please enter the second string :")
if len(commprefix(string1,string2))==0:
    print("There is no common prefix")
else:
    print("The common prefix is",commprefix(string1,string2))
