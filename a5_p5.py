#JTMS-14
#a5_p5.py
#Muskan Shah
#musshah@jacobs-university.de
 
string = input("Enter a string: ")
j = 0 
# i used as alphabet in the string and j is the position of the alphabet 
for i in string:
    print(j*" ", i)
    # incrementing j so the alphabet has new line with spaces 
    j +=1