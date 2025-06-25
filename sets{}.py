s={10,20,80,30,40,50,60}#does not allow duplicate values and it is unordered.
n=len(s)
print(n)
print("~"*50)

s1=set((100,200,300,400,800))#to create a set using set()
print(s1)
for i in s1:#to display data in each line
    print(i)
print("~"*50)

search=int(input("Enter element to search:"))
if search in s:
    print("yes")
else:
    print("no")
print("~"*50)

print(50 in s)
print("True" if 30 in s else "False")
print("~"*50)

#add()
d=s.add(100)#to include a data in the set
print(s)
print("~"*50)

#bool()
print(bool(50))
s2={}
print(bool (s2))
print("~"*50)

#update()
s.update(s1)#join two sets
print(s)
print("~"*50)

#remove()
s1.remove(800)
#s1.remove(10)#raises an error if it is not available
print(s1)
print("~"*50)

#discard()
s1.discard(200)
s1.discard(10)#does not raises an error
print(s1)
print("~"*50)

#pop()
s3={1,2,3,6}
s3.pop()#removes a random element
print(s3)
print("~"*50)

#clear()
s1.clear()
print(s1)
print("~"*50)

#del()
del(s)
print("~"*50)

#union()
set1={"a","b","c","d"}
set2={"c","d","e","f"}
set3=set1.union(set2)
print(set3)
print("~"*50)

#intersection()
set4={10,20,30,40}
set5={10,30,50,70}
"""
set6=set4.intersection(set5)#shows duplicate values from both sets
print(set6)
print("~"*50)

#intersection_update()
set6=set4.intersection_update(set5)
print(set6)
print("~"*50)
"""
#symmetric_difference_update()
set6=set4.symmetric_difference_update(set5)#shows different values in s2
print(set6)
print("~"*50)

#symmetric_difference()
#now set4={70,40,50,20}
#now set5={10,30,50,70}
set6=set4.symmetric_difference(set5)
print(set6)#except the similar ones other elements get printed

