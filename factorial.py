def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)
s=int(input("Enter a number:"))
print("Factorial of",s,"is",fact(s))
