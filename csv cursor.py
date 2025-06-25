def program7():
    f=open("Answer.txt","r")
    print("Cursor initial position.")
    print(f.tell())
    f.seek(4,0)
    print("Displaying values from 5th position.")
    print(f.read(5))
    f.seek(10,0)
    print(f.tell())
    print("Print cursor's current position")
    print(f.seek(7,0))
    print("Displaying next 10 characters from cursor's current position.")
    print(f.read(10))
program7()

OUTPUT
Cursor initial position.
0
Displaying values from 5th position.
on is
10
Print cursor's current position
7
Displaying next 10 characters from cursor's current position.
is super a
