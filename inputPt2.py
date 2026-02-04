#Prompt the user for an input
print("Hello, what's your name?")
#The "input()" function receives the user's name
username = input()

#What can we do with input?
#We can make choices! Note that in an if, you use == not = and finish it with a :
if(username == "Mr. B"):
    print("Welcome!")
    print("What is your favorite number?") #All of these are within the if because they're all "tabbed" over
    favorite_number = int(input()) #Don't forget to make it a number! (Using int())
    #Making sure to convert the number back in order to print!
    print("Well, your new favorite should be " + str(favorite_number*2)+ ", it's twice as good!")
#The else is outside of the if because it's back on the first line
else:
    #Everything on this tab line is part of the else
    print("Invalid Username!")
