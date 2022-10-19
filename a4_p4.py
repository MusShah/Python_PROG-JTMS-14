#JTMS-14
#a4_p4.py
#Muskan Shah
#musshah@jacobs-university.de
 
 
sum = 0 
count = 0 
 
for idx in range(1, 10):
    #assigning n inside the loop to ensure that it can have multiple inputs. 
    n = int(input("Enter a integer "))
    #ensuring that -9 is not included in the calculation
    if n== -9:
        print ("")
        break 
    sum += n
    count += 1 
    
#calculating and printing the average
average = sum/count
print("The average is:", round(average))