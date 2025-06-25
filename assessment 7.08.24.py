dict_1={}
dict_1["Name"]="Anika"
dict_1["Age"]=18
dict_1["Course"]="AI"
print(dict_1)

v=dict_1["Age"]
print(v)

change=dict_1.update({"Age":20})
print(dict_1)

del dict_1["Course"]
print(dict_1)

for x,y in dict_1:
    print(x,y)

kv=dict_1.items()
print(kv)

search=input()
key=dict_1.keys()
if search not in key:
    print("False")
else:
    print("True")

num=len(dict_1)
print(num)

k="Course"
if k not in key:
    print("None")
else:
    dict_1.get(k)

k="Course"
if k not in key:
    print("None")
else:
    dict_1.pop(k)
print(dict_1)

dict_1.clear()
print(dict_1)

d2={"num":123,"alpha":"abc"}
d3=d2.copy()
print(d3)

d2_key=d2.keys()
d2_value=d2.values()
d2_item=d2.items()
print(d2_key)
print(d2_value)
print(d2_item)

