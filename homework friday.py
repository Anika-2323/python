#1
L=[10,45,1,67,56]
L.sort()
print("List sorted in ascending order:",L)
s=sorted(L,reverse=True)
print("List sorted in descending order:",s)
print("~"*30)

#2
s1={10,56,35,24}
s2={56,78,29,10}
s3=s1.intersection(s2)
print("Common elements:",s3)
s4=s1.symmetric_difference(s2)
print("Uncommon elements:",s4)
s1.remove(35)
print("After removing data:",s1)
print("~"*30)

#3
T=tuple((50,46,85,42))
l=list(T)
l.append(60)
print("After appending:",tuple(l))
l.remove(50)
print("After removing:",tuple(l))
print("~"*30)

#4
text="     Welcome to my  home"
i=text.rindex("home")
print(i)
r=text.replace("h","H")
print(r)
s=text.lstrip()
print(s)
