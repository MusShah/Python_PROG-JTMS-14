#JTMS-14
#a5_p4.py
#Muskan Shah 
#musshah@jacobs-university.de
 
import random
 
random.seed()
 
minval = 1
maxval = 50
r = random . randint(minval, maxval)
# initialisng count_tries
count_tries = 0 
 
found = False
while not found:
    guess = int(input("Enter your guess: "))
    #incrementing the number of tries to find the right guess and printing the result
    count_tries += 1
    print("The number of tries: ", count_tries)
    #printing if statements for guessing the right answer. 
    if r == guess:
        print("You got it! ")
        found = True
        #using break so the game stops when the correct answer is found. 
        break
    #prininting the statements if the answer is not correct. 
    elif guess < r:
        print("Your guess is too small! ")
    else:
        print("Your guess is too high! ")
 
print(" Bye ")