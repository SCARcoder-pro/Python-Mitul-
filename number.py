import random
playing = True
number = str(random.randint(10, 20))

print("I will generate a number between 10 and 20, and you have to guess the number one didit at  a time.")
print("The game ends when you get 1 Hero.")
while playing:
    guess = input("Give me the best guess! \n")
    if number == guess:
        print("You win the game!")
        print("The number was: " , number)
        break

    else:
        print("Your guess isn't quite right, try again!")