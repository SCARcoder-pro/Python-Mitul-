import math

n = 10
p = 0.5

prob_2 = math.comb(n, 2) * (p ** 2) * ((1 - p) ** (n - 2))
prob_3 = math.comb(n, 3) * (p ** 3) * ((1 - p) ** (n - 3))
prob_4 = math.comb(n, 4) * (p ** 4) * ((1 - p) ** (n - 4))

prob_between_2_and_4 = prob_2 + prob_3 + prob_4

print("Probability of observing between 2 and 4 heads in 10 coin flips is:", round(prob_between_2_and_4, 3))