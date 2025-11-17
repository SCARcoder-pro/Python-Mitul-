import random
def roll_dice_experiment():
    dice = [1, 2, 3, 4, 5, 6]
    result = random.choice(dice)
    pro = dice.count(6) / len(dice)
    print("Probability of rolling a 6:", pro)
    if result == 6:
        print("Congrats, You rolled a 6!")
    else:
        print("Better luck next time.")

res = roll_dice_experiment()
print(res)