'''#1
n=int(input())
fib=[]
a=0
b=1
while len(fib)<n:
    c=a+b
    a=b
    b=c
    if c%2==0:
        fib.append(c)
print(fib[n-1])'''

#2
plot=int(input())
area=list(map(int,input().split()))
print(area)
temp=[]
count=0
for i in range(2,len(area)+2):
    sq=i*i
    temp.append(sq)
for i in range(len(temp)):
    if temp[i] in area:
        count+=1
print(count)
    
    
