#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 2.9
######################

print("The range of outside temperature should be within -58 to 41 and windspeed gretaer than or equal to 2")
ta=int(input("Please enter the outside temperature :"))

ws=int(input("Please enter the wind speed :"))

if ta>-58 and ta<41 and ws>=2:

    tw=35.74+0.6215*ta-35.75*ws**0.16 +0.4275*ta*ws**0.16
    print("The wind chill temperature :",tw)
else:
    print("Please enter the correct input Temperature/Wind speed")


    

    



