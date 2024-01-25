import random

user_wins = 0
computer_wins = 0
draw_match = 0

options = ['rock','paper','scissors']

while True:
    
    user_pick = input("Pick Rock/Paper/Scissors or Q to quit: ").lower()
    
    if user_pick == "q":
        break
    
    if user_pick not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    
    if user_pick == 'rock' and computer_pick == 'scissors':
        print(f"You pick {user_pick} and computer pick {computer_pick}")
        print("You won!")
        user_wins = user_wins + 1  
    elif user_pick == 'scissors' and computer_pick == 'paper':
        print(f"You pick {user_pick} and computer pick {computer_pick}")
        print("You won!")
        user_wins = user_wins + 1
    elif user_pick == 'paper' and computer_pick == 'rock':
        print(f"You pick {user_pick} and computer pick {computer_pick}")
        print("You won!")
        user_wins = user_wins + 1
    elif user_pick == computer_pick :
        print(f"You pick {user_pick} and computer pick {computer_pick}")
        print("Match draw!")
        draw_match = draw_match + 1
    else :
        print(f"You pick {user_pick} and computer pick {computer_pick}")
        print("You lost!")
        computer_wins = computer_wins + 1
        
print("You won",user_wins,"times.")        
print("Computer won",computer_wins,"times.")
print("Draw match",draw_match,"times.")      
print("Thanks for visiting.")

