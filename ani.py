RS = int(input("Enter the number of red shirts: "))
BS = int(input("Enter the number of blue shirts: "))
WS = int(input("Enter the number of white shirts: "))

total = RS+BS+WS
prob_a = BS/total
prob_b = WS/total

prob_bga = prob_b
prob_a_and_b = prob_a * prob_bga

print("Probability that the second shirt is red given that the first shirt is blue: ")
print(round(prob_bga),3)

print("Probability that the first shirt is blue and the second shirt is white: ")
print(round(prob_a_and_b,3))