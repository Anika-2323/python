def fibonacci(n):
    a,b=-1,1
    for i in range(1,n+1):
        c=a+b
        a,b=b,a
        b=c
    return(c)
num=int(input("Enter a number:"))
print("The element of the series:",fibonacci(num))
7708693543
