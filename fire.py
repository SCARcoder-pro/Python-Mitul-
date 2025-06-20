class Employee:

    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor Called")

def Create_obj():
    print("Making Object.....")
    obj = Employee()
    print("function and.....")
    return obj

print("Calling Create_obj() function.....")
obj = Create_obj()
print("Program end....")