users = ["nolan", "george", "fernando","tristan"]
passwords = ["RobloxHacker12345!", "!@#$*&^%^&*GeorgeDVtsafgdiuchjkv", "!R#Q@$WY%XE^C&RV*(BYUNP(O*YIT&U^R%EX$))","print()"]
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
#Comment
usernameinp = input("What's your username?: ")
count = 0
if (usernameinp in users):
    passwordinp = input("What's your password?: ")
    for x in users:
        if(usernameinp == x):
            break
        else:
            count = count + 1
    if(passwordinp == passwords[count]):
        print("Correct!")
    else:
        print("False")
