#define the class
class aNumber():
    x = 3

#create an instance of the class
num = aNumber()
#What happens if we just print the object?
print(num)
#We're printing now what the object holds in x
print(num.x)

#What do we get if we create another instance?
num2 = aNumber()
print(num2.x)

if(num == num2):
    print()
    print("They're the same!")
else:
    print()
    print("They're different?")

#Create a person class (example used from w3schools)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

#what do we think will be the result? How can we create another person?
#Will our new person be the same as the other, even if they have the same values?
print(p1.name)
print(p1.age)

p2 = Person("Fernando", 18)
print(p2.name)
print(p2.age)

p3 = Person()
print(p3.name)
