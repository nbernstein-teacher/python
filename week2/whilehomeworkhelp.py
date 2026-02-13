#Python help/reference for calculator programs week of 2/9

#Booleans can be set to True or False
booleanvar = True

#While booleanvar is True, run everything in this code over and over
while(booleanvar):
    #Loop jumps up to here every time it runs again
    userinp = input("Do you want to continue? (y/n): ")
    #If the user wants to continue, keep booleanvar as True
    if(userinp == "y"):
        booleanvar = True
    #If the user doesn't, set booleanvar to False. This ends the loop and goes to EXIT
    elif(userinp == "n"):
        booleanvar = False
    #If the user didn't make a proper choice, tell them!
    else:
        print("Answer either 'y' or 'n'!")

#EXIT - This is where the loop leaves to when it is sent to false
while(booleanvar):
    print("This will never print because booleanvar is False!")

#How to keep a program running if a user inputs within a range
booleanvar = True #Create a boolean to keep the loop running
while(booleanvar):
    num1 = int(input("Enter a number between 1 and 10!")) #If it's not an int, this will not be able to calculate!
    if(num1 > 0 and num1 <= 10): #If the number is greater than 0 and less than or equal to 10
        print("Good job, your number is between 1 and 10!")
        booleanvar = False #Use the boolean to exit the loop to EXIT2
    else:
        print("Try again!") #User did not enter a proper number

#EXIT2 - This is where the program jumps if the user enters a proper number
#This is where you can do whatever calculation you need with num1
