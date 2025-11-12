def prob_a_or_b(a, b, all_possible_outcomes):
    prob_a = len(a)/len(all_possible_outcomes)
    prob_b = len(b)/len(all_possible_outcomes)
    inter = a.intersection(b)
    prob_enter = len(inter)/len(all_possible_outcomes)
    return(prob_a + prob_b - prob_enter)

events= {2, 4, 6}
greater_than_two = {3, 4, 5, 6}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

print("Probablity of rolling a number greater than 2")
print(prob_a_or_b(events, greater_than_two, all_possible_rolls))