numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

even_squares = [num ** 2 for num in numbers if num % 2 == 0]

print("Original list:", numbers)
print("Squares of even numbers:", even_squares)