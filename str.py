class IOString():
    def __init__(self):
        self.str1 = ""
    
    def get_String(self):
        self.str1 = input("Enter a string: ")
        
    def print_String(self):
        print("Result is: ", self.str1.upper())

strl1 = IOString()
strl1.get_String()
strl1.print_String()