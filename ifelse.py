#Getting input from a user
print("Please enter your name!")
username = input()

#Welcome the user
print("Welcome to the jungle, "+username+".")

#Prompt the user's first decision
print("Do we have fun and games? (y/n)")
inp1 = input()

#First if/else
if(inp1 == "y"):
    print("Do we have everything you want? (y/n)")
    #this is where you'd get your next input
    whatyouwant = input()
    if(whatyouwant == "y"):
        print("We are the people that can find whatever you may need")
        print("Do you have the money, honey? (y/n)")
        money = input() #get the input
        if(money == "y"): #use the input
            print("We've got your disease, "+username+".") #tab over so it's in the if
        elif(money == "n"): #use an else if
            print("We don't have anything for you, "+username+"!") #see how we're using the username?
        else:
            print("What are you talking about "+username+"?")
    elif(whatyouwant == "n"):
        #All this is tabbed over because it's within the else if
        print("We can't find anything you want?")
        print("Well, do you want to go home? (y/n)")
        gohome = input() #get another input
        if(gohome == "y"): #use the input
            print("Welcome home, "+username+"!")
        elif(gohome == "n"):
            print("You've been eaten by the jungle.")
        else:
            print("Speak some sense, man!")
    else:
        print("You need to want something we know about!")
elif(inpt1 == "n"):
    print("It's going to bring you to your knees")
    print("Can you get up? (y/n)")
    getup = input() #get the input
    if(getup == "y"): #use the input
        print("The jungle is a serious business, "+username+", try to stay on your feet!")
    elif(getup == "n"):
        print("Watch it bring it to your n-n-n-n-n-n-n-n knees, knees, "+username+"!")
    else:
        print("Answer correctly or you won't have knees in the jungle!")
else:
    print("That's not an answer!")
