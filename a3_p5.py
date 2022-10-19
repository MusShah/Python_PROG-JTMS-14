#JTMS-14
#a3_p5.py
#Muskan Shah
#musshah@jacobs-university.de
 
character = 'c'
c = str(input ("Enter a lowercase character "))
#converting and printing the number for the letter in ASCII code. 
asc = ord(c)
print(asc)
 
#the lowercase characters in ASCII table is between 97 and 122
#if statement  ensures that any number not in this range is disregarded 
if asc >= 97 and asc <= 122:
    print("The character is a lowercase", character)
else:
    print("The character is not a lowercase", character)