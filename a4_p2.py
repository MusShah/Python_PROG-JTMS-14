#JTMS-14
#a4_p2.py
#Muskan Shah 
#musshah@jacobs-university.de
 
#defining the function 
def characters(ch, n):
    for i in range (n+1):
        #printing the result 
        print(chr(ord(ch) + i))
    return print 
 
#upper function makes sure that the alphabets are capital
ch = input ("Enter a character").upper()
n = int(input("How many characters:"))
characters(ch, n)