age = int(input("Enter your age: "))
if age >= 10:
    if age <= 20:
        print("Your age is : ", age, "\n you are allowed to enter the class")
    else:
        print("Your age is : ", age, "\n you are not allowed to enter the class")
else:
    print("Your age is : ", age, "\n you are not eligible")