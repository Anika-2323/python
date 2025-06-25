#1
import array as arr   
sales=arr.array('i',[1200,1500,1100,1700,1600,1800,1300,1900,1750,1600,1400,1500])
print(sales[6])
lis=sales.tolist()
lis.reverse()
new=arr.array('i',lis)
print(new)
ext=arr.array('i',[1600,1700])
sales.extend(ext)
print(sales)

#2
import array as a
score=a.array('i',[20,50,40,80,89,83,42,30,56,44])
score[4]=99
print(score)
new=score.tolist()
new.sort()
print("Student with the highest score is ",new[9])
print("Student with less score is",new[0])

#3
import array as e
price=e.array('d',[10.99,5.49,20.00,7.95,12.75])
li_st=price.tolist()
add=sum(li_st)
print("Total cost of the items is:",add)
li_st.remove(li_st[2])
print(li_st)
li_st.append(15.99)
print(li_st)

    
