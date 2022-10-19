#JTMS-14
#a4_p5.py
#Muskan Shah 
#musshah@jacobs-university.de
 
#defining the function for the pattern of the rectangle.
def print_rectangle(n, m ,c):
    for i in range(n): #defining rows 
        for j in range(m): #defining columns 
            print(c, end= '')
        #for new line
        print()
 
#declaring variables.                      
n = int(input("Enter a integer"))
m = int(input("Enter a integer"))
c = input("Enter a character")
#printing the result. 
print_rectangle(n,m,c)