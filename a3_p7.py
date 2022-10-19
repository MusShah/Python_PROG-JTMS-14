#JTMS-14
#a3_p7.py
#Muskan Shah 
#musshah@jacobs-university.de
 
#initialisng variables
n = int (input("Enter a number"))
i = 1
 
#calculating seconds 
# and making sure that the value of n is greater or equal to 1    
while i <= n:
    #uisng if statement for 1 minute as the first situation and 
    # the second situation is any other number for which else is used
    if i == 1:
        print("1 minute= ", i*60)
    else:
        print(i, "minutes= ", i*60)
    # incrementing i so that the loop is not infinite
    i +=1