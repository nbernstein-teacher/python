#Booleans are either "True" or "False"!
booltrue = True
#Notice how the variable changes color - try "TRUE" or "true" and it won't work!
if(booltrue == True):
    print("It was true!")

boolfalse = False
#Again, it changes color. This sets "boolfalse" to be boolfalse
if(boolfalse): #Since a boolean is already true or false, it's already true or false for an if!
    print("It was true?")
else:
    print("It was false!")

#Lets try setting a boolean with a mathematical expression!
boolfalse = (1 == 1) #This evaluates to true, so we can check if it's properly stored as True
print("After mathematical set: "+str(boolfalse)) #Don't forget to change the variable type to print!
if(boolfalse):
    print("It was true?")
else:
    print("It was false!")
