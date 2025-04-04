number1 = int(input("Enter the 1st number: "))
number2 = int(input("Enter the 2nd number: "))
number3 = int(input("Enter the 3rd number: "))

if number1 > number2 and number1 > number3:
    print("The 1st number is the greatest")
elif number2 > number1 and number2 > number3:
    print("The 2nd number is the greatest")
elif number3 > number1 and number3 > number2:
    print("The 3rd number is the greatest")