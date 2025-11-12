import random
def pick_dice_experiment():
    dice = ['1', '2', '3', '4', '5', '6']
    result = random.choice(dice)
    pro = dice.count('6') /len(dice)
    print("Probability of getting a six:", pro)
    if result == '6':
        print("Congrats! You got 6!")
    else:
        print("Better luck next time.")

res = pick_dice_experiment()
print(res)