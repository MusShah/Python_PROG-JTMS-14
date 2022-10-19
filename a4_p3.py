#JTMS-14
#a4_p3.py
#Muskan Shah
#musshah@jacobs-university.de
 
#defining the function
def characters(ch, n):
    for i in range (n+1):
        print(chr(ord(ch) + i))
 
ch = input ("Enter uppercase character: ")
#making sure that ch is capital letter by using while loop
while (ch<'A'  or ch > 'Z'):
    ch = input("Enter uppercase character: ")
#making sure that n is within the range. 
n = int(input("How many characters between 0 and 32: "))
while ((n < 0) or (n>32)):
    n = int(input("Enter a integer between 0 and 32: "))
 
characters(ch,n)