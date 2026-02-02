num1 = 3
num2 = "5"

#remember, if you take input from a user, it's always a string!
#turning num2 from a string to an integer (whole number)
print("Type of num2 before convesion: ", type(num2))
num2 = int(num2)
print("Type of num2 after convesion: ", type(num2))

#add, then print
add = num1 + num2
print("Added: ", add)

#subtract, then print
sub = num1 - num2
print("Subtracted: ", sub)

#multiply, then print
mult = num1 * num2
print("Multiplied: ", mult)

#divide, then print
divi = num1 / num2
print("Divided: ", divi)

#find the remainder, then print
rema = num1 % num2
print("Remainder: ", rema)
