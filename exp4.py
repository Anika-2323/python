import pickle
stu_dat={}
n=int(input("Enter number of students:"))
stu file=open("studat.txt","wb")
for i in range(n):
    stu_dat['name']=input("Enter name:")
    stu_dat['roll_no']=int(input("Enter roll no.:"))
    stu_dat['marks']=float(input("Enter marks:"))
    pickle.dump(stu_dat,stufile)
stufile.close()
stu_dat={}
found=False
roll_no=int(input("Enter the roll number of student:"))
stufile=open("studat.txt",'rb+')
try:
    while True:
        pos=stufile.tell()
        stu_dat=pickle.load(stufile)
        if stu_dat['roll_no']==roll_no:
            stu_dat['marks']=float(input('Updated marks:'))
            stufile.seek(pos)
            pickle.dump(stu_dat,stufile)
            found=True
except EOFError:
    if found==False:
        print("The student was not found")
    else:
        print("The marks is updated")
stufile.close()
stu_dat={}
file=open("studat.txt","wb")
try:
    while True:
        stu_dat=pickle.load(stufile)
        print(stu_dat)
except EOFError:
    stufile.close()
