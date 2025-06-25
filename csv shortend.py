
import mysql.connector as sql1
mycon=sql1.connect(host='localhost',username='root',passwd='',database='student')
cursor=mycon.cursor()
cursor.execute('SELECT*FROM student')
b=[]
x=cursor.fetchall()
print('---Updated Marks---')
roll_no=int(input("Enter roll number:"))
for row in x:
    b.append(row)
for a in range(len(b)):
    if b[a][0]==roll_no:
        updated_marks=int(input('Enter marks to update:'))
        ud='UPDATE student SET marks={} WHERE roll_no={}'.format(updated_marks,roll_no)
        cursor.execute(ud)
        print('Updated')
