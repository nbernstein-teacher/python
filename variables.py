#Defining our variables
name = "Mr. Bernstein" #This is a string because it has quotes around it
age = 23 #This is an integer (a number) because it doesn't have quotes
height = 72.75 #This is a float (decimal number) because it doesn't have quotes and has a decimal point.
favorite_food = "Pasta" #This is another string

age = float(age) #Changing age to a float
age = int(age) #Changing age to an integer
age = str(age) #Changing age to a string

#Basic print statement
print(age)

#How to print the type of a variable
print(type(age))

#How to print a string, with a varible attached to it
print("Hello, my name is:", name +".") #Comma adds a space between, + doesn't add a space

#Careful! If you add a string and a number, you'll get an error!
#Example:
#print("My name is " + name + " I am " + height + " inches tall.") - This results in an error.
#print("My name is " + name + " I am ", height, " inches tall.") - This works.
#print("My name is " + name + " I am " + str(height) + " inches tall.") - This also works, because height is changed to a string.
