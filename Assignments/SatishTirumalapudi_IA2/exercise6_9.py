#Name :Satish Tirumalapudi
#E-mail:stirumalapudi1@student.gsu.edu
#problem :Excercise 6.9
##Foot to meters and viceversa
#1 foot=0.305 meters
#1 meter=1/0.305 foot

# Convert from feet to meters
def footToMeter(foot):
    return round(foot * .305,2)
# Convert from Meters to feet
def meterToFoot(meter):
    return round((meter/.305),3)
print ("Feet \t Meters  |  Meters\tFeet")
print("------------------------------------------")
for foot, meter in zip(range(1, 11), range(20, 70, 5)):
    print ("%s \t %s \t |  %s\t      %s " % (foot, round(footToMeter(foot),3), meter, round(meterToFoot(meter),2)))