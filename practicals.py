#hanoi
''''def hanoi(n,start,temp,end):
    if n==1:
        print("Move disk 1 from rod",start,"to rod",end)
        return
    hanoi(n-1,start,end,temp)
    print("Move disk",n,"from rod",start,"to rod",end)
    hanoi(n-1,temp,start,end)
n=int(input("Enter number:"))
hanoi(n,'A','B','C')

#json
import json
from difflib import get_close_matches
data=json.load(open("dict.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Do you mean %s instead? Enter y if yes or n if no:"%get_close_matches(w,data.keys())[0])
        yn=yn.lower()
        if yn=='y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=='n':
            return "the word doesn't exit, please double check it"
        else:
            return "the word doesn't exit, please double check it"
    else:
        return "the word doesn't exit, please double check it"
word=input("Enter word:")
output=translate(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
input("Press ENTER to exit")



import numpy as np
a=np.array([[1,2],[3,4]])
a=np.array([[3,2],[3,5]])
result=np.dot(a,b)
print("result of mul:,\n",result)'''

#matrix mul
A=[]
B=[]
C=[[0,0],[0,0]]
print("Matrix 1:")
for i in range(
