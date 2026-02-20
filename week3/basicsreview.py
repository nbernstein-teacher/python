#review everything we've been through in a nice example program
#Get user inputs
#If, elif, else
#While/for loops
import time

redPoints = 0
greenPoints = 0
timeExpired = False
incorrectInput = True

#make a list of possible answers
greenAnswers = ["Green", "g", "G", "green", "GREEN"]
redAnswers = ["Red", "r", "R", "red", "RED"]

print("Welcome to basketball!")
redName = input("What is the name of the red team?: ")
greenName = input("What is the name of the green team?: ")

#add the team names to the possible answers list
greenAnswers.append(greenName)
redAnswers.append(redName)

while(timeExpired == False):
    print("Here's the tip off! Who gets the ball?")
    choice1 = input()
    if(choice1 in greenAnswers):
        while(incorrectInput):
            print(greenName + " gets the ball, they drive down the court and put up a shot")
            make = input("Do they make the bucket? (y/n): ")
            if(make == "y"):
                greenPoints = greenPoints + 2
                print("What a shot!")
                incorrectInput = False
            elif(make == "n"):
                print("HOLY AIR BALL")
                incorrectInput = False
            else:
                print("That's not a y or an n, try again!")
        #reset the boolean for future use
        incorrectInput = True
        print("The game goes on, each team scores 50 points and we're down to the final 10 seconds.")
        print("Red has the ball, down 2 points, 52 to 50")
        for num in range(10, 4, -1):
            print(num)
            time.sleep(1)
        while(incorrectInput):
            print("Does "+redName+" pass the ball? (y/n)")
            passchoice = input()
            if(passchoice == "y"):
                print("They swing it and make the 3!")
                for num in range(4, -1, -1):
                    print(num)
                    time.sleep(1)
                print("The clock runs out, "+redName+" WINS")
                timeExpired = True
                incorrectInput = False
            elif(passchoice == "n"):
                print("They play hero ball andddddd")
                for num in range(4, -1, -1):
                    print(num)
                    time.sleep(1)
                print("BRICK CITY")
                print(greenName+" wins.")
                timeExpired = True
                incorrectInput = False
            else:
                print("Make a right choice, the clock is running out!")
    elif(choice1 in redAnswers):
        while(incorrectInput):
            print(redName+" gets the ball, they drive down the court and put up a shot")
            make = input("Do they make the bucket? (y/n): ")
            if(make == "y"):
                redPoints = redPoints + 2
                print("What a shot!")
                incorrectInput = False
            elif(make == "n"):
                print("HOLY AIR BALL")
                incorrectInput = False
            else:
                print("That's not a y or an n, try again!")
        #reset the boolean for future use
        incorrectInput = True
        print("The game goes on, each team scores 50 points and we're down to the final 10 seconds.")
        print(greenName+" has the ball, down 2 points, 52 to 50")
        for num in range(10, 4, -1):
            print(num)
            time.sleep(1)
        while(incorrectInput):
            print("Does "+greenName+" pass the ball? (y/n)")
            passchoice = input()
            if(passchoice == "y"):
                print("They swing it and make the 3!")
                for num in range(4, -1, -1):
                    print(num)
                    time.sleep(1)
                print("The clock runs out, "+greenName+" WINS")
                timeExpired = True
                incorrectInput = False
            elif(passchoice == "n"):
                print("They play hero ball andddddd")
                for num in range(4, -1, -1):
                    print(num)
                    time.sleep(1)
                print("BRICK CITY")
                print(redName+" wins.")
                timeExpired = True
                incorrectInput = False
            else:
                print("Make a right choice, the clock is running out!")
    else:
        print("Try again, bozo!")
