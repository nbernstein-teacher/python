#A for loop range counter with a delay (countdown for game)
import time
for num in range(10, 0, -1):
    print(num)
    time.sleep(1)
print("BOOOOOM!")

#Use the "in" list to check for a range of answers
nameslist = ["Blake", "Tristan", "Nolan", "Evan", "George", "Muhammed", "Fernando", "Axel", "Malem"]
print("What is your name?")
name = input()
if (name in nameslist):
    print("Welcome, python student!")
else:
    print("You're not in this class!")

#Assignment should be making a new adventure game (They can keep the same story)
#Needs to track the player's health in an int
#Needs to get the player's name as an input and use throughout
#Needs to use an "in" list command of a list of possible Yes or No variations for decisions
#Needs to use a while to keep asking until it gets something in the Yes or No lists
