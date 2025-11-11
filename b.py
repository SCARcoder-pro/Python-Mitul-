import random
def pick_shirt_experiment():
    shirts = ['black', 'black', 'black', 'white']
    result = random.choice(shirts)
    pro = shirts.count('white') /len(shirts)
    print("Probability of picking a white shirt:", pro)
    if result == 'white':
        print("White shirt was picked.")
    else:
        print("Better luck next time.")

res = pick_shirt_experiment()
print(res)