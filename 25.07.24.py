#1
n=int(input())
temp=0
for i in range(1,n+1):
    if n==i*i:
        temp+=n
if temp==n:
     print(n,"is a Perfect Square")
else:
    print(n,"is not a Perfect Square")

#2
n=int(input())
for i in range(1,n+1):
    for j in range(i):
            print(i,end="*")
    print()
for i in range(n,0,-1):
    for j in range(i):
        print(i,end="*")
    print()

#3
row=int(input())
column=int(input())
for i in range(row):
    for j in range(column):
        if i==0 or i==column-1 or j==0 or j==row-1:
            print("1",end="   ")
        else:
            print("0",end="  ")
    print()
    


