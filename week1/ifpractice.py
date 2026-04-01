if("HELlO" == "HELLO"):
    print("True!")
    print("THis is true")
else:
    print("False")

choice = input("Do you want to choose 1 or 2: ")
print(choice)
if("1" == choice):
    print("Operation 1")
    x = int(input("What do you want to be x? "))
    y = int(input("What do you want to be y? "))
    print(x*y)
elif("2" == choice):
    print("Operation 2")
