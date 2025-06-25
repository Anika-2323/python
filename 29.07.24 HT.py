'''#1
try:
    string=input()
    sub=input()
    index=string.index(sub)
    print(index)
except ValueError as s:
    print("Substring was not found")'''

#2
try:
    grades=list(map(int,input().split()))
    avg=sum(grades)/len(grades)
    print(avg)
except:
    print("List can't be empty")

#3
try:
    num=[12,4,13,9]
    print(num[4])
except IndexError as i:
    print("Index out of range")
    

