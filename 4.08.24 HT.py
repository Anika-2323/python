#1
import array as a
N=int(input())
arr=a.array('i')
count=0
for i in range(N):
    arr.append(int(input()))
elem_search=int(input())
for i in arr:
    if elem_search==i:
        count+=1
if count<N/2:
    print(elem_search,"is not a majority element")
else:
    print(elem_search,"is a majority element")

#2
import array as a
n=int(input())
arr=a.array('i')
for i in range(n):
    arr.append(int(input()))
lst=arr.tolist()
lst.sort()
lar=lst[n-2]
print("The second largest element is",lar)
        
#3
num=input()
old=input()
new=input()
new_lst=num.replace(old,new)
print("Modified number =",new_lst)

#4
login_dict={"anika":"1234","janhavi":"5678","archana":"91011","abi":"1213"}
username=input("Enter username:")
keys=login_dict.keys()
value=login_dict.values()
if username in keys:
    password=input("Enter password:")
    if password not in value:
        print("Incorrect password")
    else:
        print("Successfully logged in.")
else:
    print("Invalid username")
    
        


