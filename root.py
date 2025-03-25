Amount = int(input("Enter the amount: "))
note_1 = Amount // 100
note_2 = (Amount % 100) // 50
note_3 = ((Amount % 100) % 50) // 10

print("Notes of 100 rupees: ", note_1)
print("Notes of 50 rupees: ", note_2)
print("Notes of 10 rupees: ", note_3)


print("\nEnter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))


sum_marks = math + english + science + hindi
print("Sum of math, english, science and hindi: ", sum_marks)

perc = (sum_marks / 400) * 100

print(end="Percentage Mark = ")
print(perc)

tree1 = 98
tree2 = 94
tree3 = 41
tree4 = 95
tree5 = 11

sum_trees = tree1 + tree2 + tree3 + tree4 + tree5
print("\nThe sum of all 5 trees is: ", sum_trees)
average = sum_trees / 5
print("The average height of all 5 trees is: ", average)