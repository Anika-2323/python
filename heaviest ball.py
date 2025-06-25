b1=25
b2=5
b3=30
if b1>b2:
    del(b1)
    second1=b2
else:
    del(b2)
    second1=b1
if b2>b3:
    del(b2)
    second2=b3
else:
    del(b3)
    second2=b2
if second1>second2:
    del(second2)
    second=second1
else:
    del(second1)
    second=second2
print(second)
