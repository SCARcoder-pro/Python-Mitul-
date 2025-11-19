RB = int(input("Enter the number of red bus: "))
BB = int(input("Enter the number of blue bus: "))
WB = int(input("Enter the number of bus: "))

total = RB+BB+WB
prob_a = BB/total
prob_b = WB/total

prob_bga = prob_b
prob_a_and_b = prob_a * prob_bga

print("Probability that the second bus is red given that the first bus is blue: ")
print(round(prob_bga),3)

print("Probability that the first bus is blue and the second bus is white: ")
print(round(prob_a_and_b,3))