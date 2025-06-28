import random
playing = True
number = str(random.randint(10,20))
print("A number between 10 and 20 will be generated. You have to guess the number one digit at a time")
print("The game ends when you get 1 hero!")
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("It is incorrect. Try again")