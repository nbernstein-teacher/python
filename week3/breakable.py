supersecret = "Hello!"
allowed = ["1+1", "1+2", "1+3"]
userinp = input("Give me an equation! ")
#Actually working filtering
if(userinp in allowed):
    print(eval(userinp))
else:
    print("Nice try")

#broken with "exec('pr'+'int(supersecret)')"
#if("print" in userinp):
    #print("Nice try")
#else:
    #print(eval(userinp))
