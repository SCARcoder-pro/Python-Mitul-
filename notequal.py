string = input("Please enter your own string: ")
string2 = ('')
for i in string:
    string2 = i + string2
print("\n The Original string =", string)
print("\n The Reversed string =", string2)