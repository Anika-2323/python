import array as arr
num=arr.array('i',[2,3,4,5])
list1=num.tolist()
list1.sort()
list1.sort(reverse=True)
rev_arr=arr.array('i',list1)
for i in rev_arr:
    print(i,end=" ")
