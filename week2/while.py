count = 0
while(count < 10):
    count = count+1
    print(count)

print("Do we have fun and games? (y/n)")
inp1 = input()
while(inp1 != "y" and inp1 != "n"):
    print("Do we have fun and games? (y/n)")
    inp1 = input()

print("Choice:"+inp1)
