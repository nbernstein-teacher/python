class Robot:
    #Initialize what is a robot
    def __init__(self, name, productionyear, motto):
        self.name = name
        self.productionyear = productionyear
        self.motto = motto

    #Create a function for the robot to do the robot
    def dodarobot(self):
        print("Domo arigato, Mr. Roboto")

    #Create a function for the robot to print its information
    def printRobot(self):
        print("My name is " + self.name)
        print("I was made in " + str(self.productionyear))
        print(self.motto)

    #Create a function to check if the robot is unc
    def isunc(self, curryear):
        if((curryear-20) > self.productionyear):
            print("UNC ROBOT")
        elif((curryear-10) > self.productionyear):
            print("You're kinda old")
        else:
            print("You're just a baby robot!")

#Create a robot, stored in the variable "terminator"
terminator = Robot("Terminator", 1984, "Hasta la vista, baby.")
#Call the function printRobot using our newly created terminator
terminator.printRobot()
#Ask the terminator to do the robot
terminator.dodarobot()
#Check if the terminator is unc
terminator.isunc(2026)
#Check if the terminator was unc in the 90s
terminator.isunc(1990)
