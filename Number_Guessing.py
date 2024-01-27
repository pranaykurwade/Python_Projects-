import random 

top_of_range =input("Enter any number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("Enter the number greater than 0 next time !")
        quit()
else :
    print("Enter the number next time")
    quit()

random_number = random.randint(0,top_of_range)

guesses = 0

while True :
    guesses = guesses + 1
    
    user_number = input("Enter the number: ")
    if user_number.isdigit():
        user_number = int(user_number)
    else: 
        print("Enter the number next time") 

    if random_number == user_number:
        print("You guess correctly :) ")
        break
    elif user_number<random_number:
        print("You are below the number")
    else:
        print("You are above the number")
         
print("You got in",guesses,"guesses")