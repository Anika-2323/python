import mysql.connector as sql1
mycon=sql1.connect(host='localhost',user='root',passwd='',database='student')
cursor=mycon.cursor()
cursor.execute("SELECT*FROM student")
b=[]
x=cursor.fetchall()
print("---Updated marks---")
rollno=int(input("Enter rollno"))
for row in x:
    b.append(row)
for a in range(len(b)):
    if b[a][0]==rollno:
        updated_marks=int(input("Enter updated marks:"))
        ud="UPDATE student SET marks={} WHERE roll_no={}".format(updated_marks,rollno)
        cursor.execute(ud)
        print("updated")
        break


    
