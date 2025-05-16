import random
options = ["rock", "paper", "scissors"]
user_choice= input("Choose rock, paper or scissors: ")
computer_choice = random.choice(options)
print("You chose:", user_choice)
print("Computer chose:", computer_choice)
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
     print("Rock crushes scissors! You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("Paper covers rock! You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("Scissors cut paper! You win!")
else:
    print("You Lose!")