 
# Guess Game
import random

UserRange = int(input("Enter Range, Last number...eg.50 = ")) # Takes user's range by entering last number of the range 
print("Statistics ==> Probability of Winning : ",(3/UserRange),"") # Outputs the chance stats 
trial = 0 # initialise and set trial variable 
GuessRange = list(range(1, UserRange +1 )) # create range of numbers 
SecretNumber = random.choice(GuessRange) # use the random module and the choice function to get a number
while True: # initialise and create loop 
    UserNumber = int(input("Enter your number = ")) # Enter your guess 
    trial +=1 # increase trial by one 
    if SecretNumber == UserNumber:
        print("Congrats , Winner ", "you won at the {} time".format(trial))
        break
    else:
        print("Sorry, try again")
    if trial == 3:
        print("Right Number =  ", SecretNumber)
        break


