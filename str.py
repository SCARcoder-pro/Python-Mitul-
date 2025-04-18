string = input("Please enter your own word: ")
char = input("Please enter a character: ")
i = 0
count = 0
while( i < len(string)):
    if string[i] == char:
        count += 1
    i += 1

print("The total Number of Times", char, "has occured = ", count)