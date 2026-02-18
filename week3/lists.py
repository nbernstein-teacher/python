#Lists example

#Each list item is seperated by a comma, and the entire list is surrounded with square brackets []
list1 = ["Hello", "my", "name", "is", "Mr. B"]

#lists start at 0 for the first item, like so
listpositions = [0, 1, 2, 3, 4]

listnums = [1, 2, 3, 4, 5]

#So, what will this print?
print(list1[0])

#What about this one?
print(listnums[2])

#So, if we wanted to print the whole of list1, how can we do it?
print(list1)
#This looks kind of ugly though, right?
#So, what if we used a while loop to go through it?
booleanvar = True
num1 = 0
#This works, but is kind of clunky and only works for exactly a list of size 5
while(booleanvar):
    print(list1[num1])
    if(num1 == 4):
        booleanvar = False
    else:
        num1 = num1 + 1

#What if we could know exactly what the length of the list is?
#Well, we can!
length = len(list1)
print(length)
