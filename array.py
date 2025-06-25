#space seperated string
s=input().split()
print(s)

#space seperated numbers
s=list(map(int,input().split()))
print(s)

#To get user input
import array as arr
ans=arr.array('i')
n=int(input("Enter the number of elements to be inserted:"))
for i in range(n):
    ans.append(int(input()))
for i in range(n): #print using range()
    print(ans[i],end=" ")
for i in ans: #print using array
    print(i,end=" ")

#String cannot be used
#Strings can be used in the form of list
#Only int, float and characters can be used
#Lists are most appropriate data structure
