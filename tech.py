#Sum of the elements
import array as arr
n=arr.array('i')
temp=0
num=int(input("Enter the number of elements:"))
for i in range(num):
    n.append(int(input()))
for i in range(num):
             temp+=n[i]
print("Sum of elements:",temp)

#occurrence of an element
import array as r
s=r.array('i')
ele=int(input())
count=0
for i in range(ele):
    s.append(int(input()))
search=int(input("Enter element to be searched:"))
for i in range(ele):
    if search==s[i]:
        count+=1
print(count)

#Largest element
import array as a
l=[]
largest=0
d=a.array('i',l)
elem=int(input())
for i in range(elem):
    l.append(int(input()))
for i in range(elem):
    if l[i]>largest:
        largest=l[i]
print(largest)
             
