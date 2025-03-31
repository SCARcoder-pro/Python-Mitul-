height = int(input("Enter your height in cm: "))
marks = int(input("Enter your marks: "))

if height > 180 or marks > 60:
    print("You are allowed to join the police force")
elif height < 180 or marks < 60:
    print("You are not allowed to join the police force")