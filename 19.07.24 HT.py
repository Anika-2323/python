#1
start=int(input("Start range="))
end=int(input("End range="))
print("Odd numbers:")
for i in range(start,end):
    if i%2==1:
        print(i,end=" ")
print()
print("Even numbers:")
for i in range(start,end):
    if i%2==0:
        print(i,end=" ")

#2
string="Holiday"
for i in range(len(string)-1,-1,-1):
    n=string[i]
    print(n.upper(),end=" ")

#3
num=int(input("Enter the no. of values:"))
sales_fig=[]
succ_count=0
loss_count=0
for i in range(num):
    n=int(input())
    sales_fig.append(n)
print("Sales_fig=",sales_fig)
for j in sales_fig:
    if j>0:
        succ_count+=1
    else:
        loss_count+=1
print("Number of successful sales:",succ_count)
print("Number of loss of sales:",loss_count)
