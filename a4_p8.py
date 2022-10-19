#JTMS-14
#a4_p8.py
#Muskan Shah 
#musshah@jacobs-university.de
 
#defining the function for conversion of miles into kilometers.
def convert(miles):
    kilometers = miles* 1.609344
    return(kilometers)
 
#declaring input.
#calculating and printing the result of the conversion. 
miles = float(input("Enter a number"))
print("The answer in kilometers is", convert(miles))