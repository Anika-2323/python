d={"Name":"Anika","Age":18,"Numbers":[15,20,63,45]}
print (d)
print(d["Name"])
print(len(d))
print("~"*20)

d1=dict(fruit="Apple", pet="dog", veg="carrot")
print(d1)
print(d1.get("veg"))
print("~"*20)

k=d.keys()
print(k)
print("~"*20)

d["Age"]=20
print(d["Age"])
print("~"*20)

m=d.fromkeys("Name","Anika")
print(m)
print("~"*20)
3
 
v=d.values()
print(v)
print("~"*20)

kv=d.items()
print(kv)
print("~"*20)

d.update({"Age":18})
print(d)
print("~"*20)

d["Course"]="AI"
print(d)
print("~"*20)

d.pop("Numbers")
print(d)
print("~"*20)

for i in d:
    print(i)
print("~"*20)

for i in d:
    print(d[i])
print("~"*20)

for x,y in d.items():
    print(x,y)
print("~"*20)

f=d.copy()
print(f)
print("~"*20)

d.popitem()
print(d)
print("~"*20)

del d["Age"]
print(d)
print("~"*20)


