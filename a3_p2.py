#JTMS-14
#a3_p2.py
#Muskan Shah 
#musshah@jacobs-university.de
 
str1 =  input ("Enter a string ")
int1 = int(input("Enter a integer "))
print("The multiplication answer is ", str1*int1)
#instead of giving a typical answer of multiplication. 
# the int1 will specify how many times str1 will be mentioned.
#  For example if str1 is 2 and int1 is 3 
# then the answer will be 222
 
int2 = input("enter a integer ")
int3= input ("enter a integer ")
print("The addition answer is ", int2+int3)
#instead of giving a typical answer of addition. 
#the values of int2 and int3 will be joined together for example. 
#If int2 is 4 and int3 is 3 
#then the answer will be 43
 
str2 = input("Enter a string ")
float1 = float(input("Enter a float "))
print("The multiplication answer is ", str2*float1)
#this will give a error because in python string and float cannot be multiplied. 
# the code will run if both are floats.
# Hence the correct code is 
#float1 = float(input("Enter a float"))
#float2 = float(input("Enter a float"))
#print("The multiplication answer is", float1*float2)