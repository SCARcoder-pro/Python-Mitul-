try:
    num1 = int(input("Enter your first number:"))
    num2 = int(input("Enter your second number:"))
    result = num1/num2
    print("Result is:", result)
    print("Result is". result1)

except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter a numerical value")
except NameError as ex:
    print("The exception is:", ex)

except:
    print("Some error occured")
finally:
    print("I will execute no matter what happens")