#JTMS-14
#a5_p1.py
#Muskan Shah 
#musshah@jacobs-university.de
 
#initializing variables
cup = float(input("Enter the volume of cups: "))
gallon = float(input("Enter the volume of gallon: "))
 
#defining the function for converting gallon and cup to liters and summing them up. 
def to_liter(gallon, cup):
    cup = cup * 0.2366
    gallon = gallon * 3.7854
    sum = cup + gallon
    return sum
 
#printing the result. 
print("The sum of cups and gallons in liters is: ", to_liter(gallon, cup))