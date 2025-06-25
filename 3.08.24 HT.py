#1
'''n=int(input()) #4
a=[]
for i in range(n):
    a.append(int(input())) # 2 -8 7 -7
j=0
for i in range(0,n):
    if a[i]<0: # a[0]<0? | a[1]<0? | a[2]<0? |a[3]<0?
        t=a[i] # t=-7
        a[i]=a[j] # a[3]=2
        a[j]=t # a[1]=-7
        j=j+1 #j=2
print(a) # -8 -7 7 2'''

#2
char='A'
n=4
for i in range(1,n+1):
    for j in range(i):
            print(char,end="   ")
            char=chr(ord(char)+1)
    print()

#3
'''OUTPUT:
11
13
15
17
19

#4
x=3
for i in range(x,9,2):
    print(i*10)
    

#5
import array as a
n=int(input())
arr=a.array('i')
for i in range(n):
    arr.append(int(input()))
lst=arr.tolist()
seen=set()
duplicate=set()
for i in lst:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
dup=sorted(duplicate)
for i in dup:
    print(i,end="   ")'''

    
    



























        

                   
