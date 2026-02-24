#Function creation - put "def" in front of it
def sayHello():
    print("Hello Everyone!")

#Run the function!
sayHello()

#Functions can also return things
def returnHello():
    return "Hello returners!"

#We can save it to a variable
printString = returnHello()
print(printString)

#Or we can just print it right from there!
print(returnHello())

#Functions can also take inputs!
def printWhatever(inp):
    #Whatever we put in the parantheses is now called inp!
    print(inp)

#So now printString gets put into "inp" in the function
printWhatever(printString)

#Functions are helpful for repetitive code, especially calculations!
#If we had code like this:
team1success = 85
totalteam1 = 100
rate1 = (team1success/totalteam1) * 100
print("Rate 1: "+rate1)

team2success = 42
totalteam2 = 50
rate2 = (team2success/totalteam2) * 100
print("Rate 2: "+rate2)

#We could use a function to make it easier and cleaner!
def success(successrate, totalrate):
    #What could be a good way for us to check if these are ints and calculable?
    rate = (successrate/totalrate) * 100
    print("Success rate: "+ rate)

#This function has two inputs or "parameters", so it needs two things in the parantheses!
success(85, 100)

#What would happen if we only gave it one? More than one?
#success(85)
#success(85, 100, 15)
