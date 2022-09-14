#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 4.27
######################
#Phone keypad
# We use dictionaries to get the output
char=input("Please enter a character :")
ch1=char.lower()
if ch1 in ['a','b','c']:
    print("The mapping found on telphone is 2")
elif ch1 in ['d','e','f']:
    print("The mapping found on telphone is 3")
elif ch1 in ['g','h','i']:
    print("The mapping found on telphone is 4")
elif ch1 in ['j','k','l']:
    print("The mapping found on telphone is 5")
elif ch1 in ['m','n','o']:
    print("The mapping found on telphone is 6")
elif ch1 in ['p','q','r','s']:
    print("The mapping found on telphone is 7")
elif ch1 in ['t','u','v']:
    print("The mapping found on telphone is 8")
elif ch1 in ['x','y','z']:
    print("The mapping found on telphone is 9")
else:
    print("Enter a Correct input(character) ")



