import random

def Check(user,comp):
    if (user==comp):
        return 0
    elif (user == 2 and comp == 1):  
        return -1
    elif (user == 1 and comp == 0):  
        return -1
    elif (user == 0 and comp == 2):
        return -1
    else :
        return 1

user=int(input("0 for Snake 1 for Water 2 for Gun :"))
comp = int (random.randint(0,2))

print("You :",user)
print("Computer :",comp)

score = Check(user,comp)

if (score == 0):
    print("You draw")
elif (score == -1):
    print("You loss")
else:
    print("You won")

