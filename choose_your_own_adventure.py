name = input ("enter your name: ")
print("Welcome",name,"to the adventure!")

answer = input("You come to dirty road and it comes to end you can go left or right, Which way you like to go (right/left)? ").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Which thing you want to do (swim/walk)? ").lower()
    if answer == 'swim':
        print("You swim across and were eatten by alligator.")
    elif answer == 'walk':
        print("You walk for a miles and ran out of the game. You lost!")
    else:
        print("Is not a valid.You lost!")
    
elif answer == "right" :
    answer = input("You come to a bridge,it looks like wobbly, do you want to cross it or head back (cross/back)? ").lower()
    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk with him (yes/no)? ").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold, You win!")
        elif answer == 'no':
            print("You ignore the stranger, You Lost!")
        else:
            print("Is not a valid.You lost!")
    elif answer == 'back' :
        print("You go back and Lost!")
    else :
        print("Is not a valid.You lost!")
    
    
else :
    print("Is not a valid.You lost!")

print("Thank you",name,"for visiting.")