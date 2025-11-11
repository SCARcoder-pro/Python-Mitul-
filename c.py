import random
def pick_ball_experiment():
    balls = ['red', 'green', 'blue']
    result = random.choice(balls)
    pro = balls.count('red') / len(balls)
    print("Probability of picking a red ball:", pro)

    if result == 'red':
        print("Red ball was picked.")
    else:
        print("Better luck next time.")

res = pick_ball_experiment()
print(res)