#JTMS-14
#a4_p6.py
#Muskan Shah 
#musshah@jacobs-university.de
 
#defining the function
def print_frame(n,m,c):
    for i in range(n): #defining rows
        for j in range(m): #defining columns
            #giving the if statement for where stars are needed 
            #and the else statement where stars are not needed
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                print(c, end="")
            else:
                print(" ", end= "")
        #for new line 
        print()
 
#declaring variables
n = int(input("Enter a integer"))
m = int(input("Enter a integer"))
c =input("Enter a character")
print_frame(n,m,c)