#Tracing test one - build a decision tree based on this code!
booleanvar = True

while(booleanvar):
    userinp = input("Continue? (y/n): ")
    if(userinp == "y"):
        booleanvar = True
    elif(userinp == "n"):
        booleanvar = False
    else:
        print("Invalid input")
