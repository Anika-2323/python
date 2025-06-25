#1
n=int(input())
dig=0
while n>0:
    temp=n%10
    dig+=temp
    n=n//10
print(dig)

#2
n=int(input())
dig=1
while n>0:
    temp=n%10
    dig*=temp
    n=n//10
print(dig)

#3
num=int(input())
for i in range(num,0,-1):
    print(i,end="   ")

