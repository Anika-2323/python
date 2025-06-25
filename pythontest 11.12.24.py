First_Name=input("Enter First Name:")
new=""
for i in First_Name:
    if not i.isnumeric():
        new+=i
print("Hi! Your Entered Input is",new)

#2
Name=input("Enter Name:")
Char="'"
Num_s=""
for i in Name:
    if i.isalpha() and not i.isnumeric():
        Char+=i
    if not i.isalpha() and not i.isnumeric():
        Num_s+=i
print("Your Entered Characters are-",Char)
print("Your Entered Special Characters are-",Num_s)
