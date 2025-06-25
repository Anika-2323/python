#1
n1=int(input())
L1=[]
for i in range(n1):
    L1.append(input())
n2=int(input())
L2=[]
for i in range(n2):
    L2.append(int(input()))
for j in range(n1):
        print(f"{L1[j]}  {L2[j]}")

#2
import array as a
array1=a.array('i')
n=int(input())
for i in range(n):
    array1.append(int(input()))
minimum=array1[0]
for i in range(n):
    if array1[i]<minimum:
        minimum=array1[i]
print(minimum)

#3
import array as arr
arr1=arr.array('i')
n1=int(input())
for i in range(n1):
    arr1.append(int(input()))
lst1=arr1.tolist()
lst1.sort(reverse=True)
arr2=arr.array('i')
n2=int(input())
for i in range(n2):
    arr2.append(int(input()))
lst2=arr2.tolist()
lst2.sort(reverse=True)
merge=lst1+lst2
print(merge)



    
