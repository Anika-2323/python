n=int(input())
if n%2==0:
    print("Even")
else:
    print("Odd")

n=int(input())
if n<0:
    print("Negative")
elif n>0:
    print("Positive")
else:
    print("Zero")

math=int(input())
phy=int(input())
chem=int(input())
total=math+phy+chem
percentage=total/300*100
print(total)
print(f"{percentage:.2f}")
if percentage>90:
    print("Eligible")
else:
    print("Not Eligible")

s=input()
if s.isupper():
    print("Uppercase")
elif s.islower():
    print("Lowercase")
else:
    print("Combination of both")
