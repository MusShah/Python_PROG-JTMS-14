#JTMS-14
#a3_p4.py
#Muskan Shah 
#musshah@jacobs-university.de
 
number = int(input("enter a number"))
 
#the number will be 0 if the number is completely divisible by 11. 
remainder = number%11
 
#if statement ensures that the remainder should be 0.
if remainder == 0:
    print("The number is divisible by 11", remainder)
else:
    print ("The number is not divisible by 11", remainder)