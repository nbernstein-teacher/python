#Getting input from a user
print("Please enter your name!")
username = input()

#Getting user preferences
print("Do you like chocolate? (y/n)")
choc = input()
print("Do you like bananas? (y/n)")
banan = input()
print("Do you like ice cream? (y/n)")
icec = input()
print("Do you like yogurt? (y/n)")
yog = input()

if(choc == "y" && banan == "y" && icec == "y"): #You can have as many conditions as you want!
    print("You should have a banana split!")
elif(banan == "y" && yog == "y"): #This is another "and" condition, this says if banana is y AND yogurt is y
    print("You should have a parfait!")
elif(choc == "y" && icec == "y"): #Another example of an "and"
    print("You really need to try double fudge ice cream!")
elif(icec == "y" || yog == "y"): #This is an "or" condition - this says else if ice cream is y or yog is y
    print("You must love vanilla!")
else:
    print("You must love some nasty combos!")
