print("Welcome to the Quiz !")

playing = input("Do you want to paly Quiz? ")
a = playing.lower()
if a == "yes":
    print("Let's Play :) ")
else :
    print("Thanks for Visting.")
    
score = 0
    
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print("Correct :) ")
    score = score + 1
else :
    print("Incorrect :( ")
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit" :
    print("Correct :) ")
    score = score + 1
else :
    print("Incorrect :( ")
    
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory" :
    print("Correct :) ")
    score = score + 1
else :
    print("Incorrect :( ")
    
answer = input("What does SRAM stand for? ")
if answer.lower() == "static random access memory" :
    print("Correct :) ")
    score = score + 1
else :
    print("Incorrect :( ")
    
answer = input("What does CS stand for? ")
if answer.lower() == "computer science" :
    print("Correct :) ")
    score = score + 1
else :
    print("Incorrect :( ")
    

answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive" :
    print("Correct :) ")
    score = score + 1
else :
    print("Incorrect :( ")
    
answer = input("What does OS stand for? ")
if answer.lower() == "operating system" :
    print("Correct :) ")
    score = score + 1
else :
    print("Incorrect :( ")

answer = input("What does ALU stand for? ")
if answer.lower() == "arithmetic logic unit" :
    print("Correct :) ")
    score = score + 1
else :
    print("Incorrect :( ")

answer = input("What does IT stand for? ")
if answer.lower() == "information technology" :
    print("Correct :) ")
    score = score + 1
else :
    print("Incorrect :( ")
    
answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory" :
    print("Correct :) ")
    score = score + 1
else :
    print("Incorrect :( ")
    
print("You got",str(score)+"correct questions !")
print("You got",str((score / 10) * 100)+"%.")