#Booleans are either "True" or "False"!
booltrue = True
#Notice how the variable changes color - try "TRUE" or "true" and it won't work!
if(booltrue == True):
    print("It was true!")

bool1 = False
#Again, it changes color. This sets "bool1" to be bool1
if(bool1): #Since a boolean is already true or false, it's already true or false for an if!
    print("It was true?")
else:
    print("It was false!")

#Lets try setting a boolean with a mathematical expression!
bool1 = (1 == 1) #This evaluates to true, so we can check if it's properly stored as True
print("After mathematical set: "+str(bool1)) #Don't forget to change the variable type to print!
if(bool1):
    print("It was true?")
else:
    print("It was false!")

while(bool1):
