medical_cause = input("Enter the medical cause Y or N: ")
atten = int(input("Enter the attendance of the student: "))
if medical_cause == "Y":
    if atten >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")