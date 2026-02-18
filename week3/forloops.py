#Let's use for loops with a list!
#Each list item is seperated by a comma, and the entire list is surrounded with square brackets []
list1 = ["Hello", "my", "name", "is", "Mr. B", "Haha"]

#A for loop has two parts, the variable that counts (x in this case)
#and what we're counting through (our list1 for this example)

for x in list1:
    print(x)

#This is a much easier way to count through a list, right?
#What if we want to stop after we get to "Mr. B"?

#Let's go through the list
for x in list1:
    #and let's keep printing
    print(x)
    #until we find "Mr. B"
    if(x == "Mr. B"):
        #The break command stops the for loop and jumps to "EXIT"
        break

#EXIT - This is where the loop exits after the break

#for loops can also be used for getting patterns of numbers!
#the range function has a (start, end, step)
#where step is how many it skips each time!
for y in range(0,100,5):
    #see what this prints!
    print(y)
