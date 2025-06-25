#1
num=4
for i in range(8):
    mul=num*i
    print(mul,end="   ")

#2
print("Rows and columns from the user")
row=int(input())
column=int(input())
for i in range(row):
    for j in range(column):
        print("&",end="     ")
    print()

#3
scores=[85,90,-5,76,92,-1,88,79,55]
for i in scores:
    if  i==-1:
        print("Encountered missing data. Stopping processing.")
        break
    elif i<-1:
        print("Invalid score -5 encountered. Skipping")
        continue
    else:
        print("Score:",i)

