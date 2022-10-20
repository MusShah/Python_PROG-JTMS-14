#JTMS-14
#a5_p3.py
#Muskan Shah 
#musshah@jacobs-university.de
 
#importing math because pi is used to calc the vol. 
import math
 
#intialising radius of the sphere.
r = float(input("Enter the radius of the sphere: "))
 
#defining the function for calculating volume.
def volumeSphere(r):
    volume = 4/3*math.pi*r**3
    return volume
 
#printing the output. 
print("The volume of the sphere is: ", volumeSphere(r))