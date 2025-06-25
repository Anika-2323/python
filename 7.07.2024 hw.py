#1
a=int(input())
b=int(input())
if a>b:
    print(b)
else:
    print(a)
print("~"*40)

#2
p=float(input())
n=float(input())
r=float(input())
compound=p*(1+n/100)**r
comp_interest=int(compound-p)
print("Compound interest is:",comp_interest)

#3
a=int(input())
b=int(input())
print(f"{b}  {a}")

#4
L=[50,10,84,12,63]
if 52 in L:
    print("Present")
else:
    print("Not present")

#5
S="Iam a good girl"
if "bad" not in S:
    print("True")
else:
    print("False")
