#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 7.17 
##Anagrams

string1=input("Please enter the string1 :")
string1=string1.lower()
string2=input("Please enter the string2 :")
string2=string2.lower()
def isAnagram(s1, s2):
    sorted_string1=sorted(s1)
    sorted_string2=sorted(s2)
    if(sorted_string1==sorted_string2):
        print(s1+" and "+s2 +" are anagrams")
    else:
        print(s1+ "and "+s2+" are not anagrams")

isAnagram(string1,string2)