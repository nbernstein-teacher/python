#(-b+-sqrt(b^2-4ac))/2a
import math

print("What are your variables?")
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

upperLimit = (((-1*b)+math.sqrt((b**2)-(4*a*c))/(2*a)))
lowerLimit = (((-1*b)-math.sqrt((b**2)-(4*a*c))/(2*a)))

print("Upper limit: "+str(upperLimit))
print("Lower limit: "+str(lowerLimit))

print("What is the radius of your circle?")
radius = float(input("R: "))

area = math.pi * (radius**2)

print("Area: "+str(area))
