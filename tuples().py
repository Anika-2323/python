t=("vijay","trisha","anushka")#create a tuple
print(t)
t1=(10,)#tuple with single value
print(t1)
#tuple constructor
t2=tuple((10,20,30))
print(t2)
#nagative indexing
#range of indexes
#check if item exists
#update tuples-it can be converted into list, make the update and then change it again to tuple
L=list(t)
L.append("Dulquer")
L.append("Sai pallavi")
tup=tuple(L)
print(tup)
#add two tuple
y=("Rashmika",)
t+=y
print(t)
#remove
t1=(10,20,40,50)
l=list(t1)
l.remove(50)
tupl=tuple(l)
print(tupl)
#del
del t1
#unpacking
(V,T,A,R)=t
print(V)
print(T)
print(A)
print(R)
print(t)
