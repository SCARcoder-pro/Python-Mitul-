def find_prob(a, b):

    if a == 1:
        prob_a = 0.2
        if b == 1:
            prob_bga = 0.85
        elif b == 2:
            prob_bga = 0.15
        else:
            print("Invalid Choice")
            return
        prob_a_and_b = prob_a * prob_bga
        print("Probablity of b given a", prob_bga)
        print("Probablity of both the events occuring", prob_a_and_b)

    elif a == 2:
        prob_a = 0.8
        if b == 1:
            prob_bga = 0.02
        elif b == 2:
            prob_bga = 0.98
        else:
            print("Invalid Choice")
            return
        prob_a_and_b = prob_a * prob_bga
        print("Probablity of b given a", prob_bga)
        print("Probablity of both the events occuring", prob_a_and_b)

    else:
        print("Invalid Choice")

print("Lets claculate probablity. Please enter choices for the evnts....")
print("Person has a step throat?\n1. Yes\n2. No")
a = int(input("Enter your choice(1/2): "))

print("Person has tested positive?\n1. Yes\n2. No")
b = int(input("Enter your choice(1/2): "))
find_prob(a, b)