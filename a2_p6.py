#JTMS-14
#a2_p6.py
#Muskan Shah 
#musshah@jacobs-university.de
 
#importing this so decimal representation can be done. 
from decimal import Decimal
 
 
value = int(input("Enter a number"))
#printing the diff representations of value 123
print("decimal=", Decimal(value))
print("octal=", oct(value))
print("hexadecimal=", hex(value))