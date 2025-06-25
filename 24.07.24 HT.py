#1
n=int(input())
temp=n
add=0
while temp!=0:
    digi=temp%10
    add+=digi
    temp//=10
if n%add==0:
    print(n," is a Harshad Number")
else:
    print(n," is not a Harshad Number")

#2
items=int(input())
book=[]
add=0
for i in range(items):
    n=int(input())
    book.append(n)
for i in range(len(book)):
    add+=book[i]
print("The total number of books read by all the students is:",add)

#3
n=int(input())
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()
