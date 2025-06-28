import random
options = ["Rock", "Paper", "Scissors"]
user_choice = input("Choose Rock, paper, or scissors")
computer_choice = random.choice(options)
print("Your choice", user_choice)
print("Computer's choice is", computer_choice)
if user_choice == computer_choice:
    print("It is a tie")
elif user_choice == "Rock" and computer_choice == "scissors":
    print("Rock smashes scissors. You win!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers rock. You win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissor cuts paper. You win!")
else:
    print("You loose!")