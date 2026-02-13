#Print a question to the user
print("Hello, what is your name?:")
#Get input from user
name = input()
#Print the name to test it
print(name)

#Why doesn't this print the age multiplied properly?
print("What is your age?")
#Wrapping the input with "int()" changes the characters to numbers
age = int(input())
#Set age to age times 2
age = age*2
print("Oh, so you're ", age, "years old?")
