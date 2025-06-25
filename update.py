import pickle
stu1={'rollno.':1,'name':'Anika','marks':98}
stu2={'rollno.':2,'name':'Mithra','marks':96}
stu3={'rollno.':3,'name':'Sahana','marks':95}
stu4={'rollno.':4,'name':'Shri','marks':97}
stufile=open('marks.dat','wb')
pickle.dump(stu1,stufile)
pickle.dump(stu2,stufile)                                   
pickle.dump(stu3,stufile)
pickle.dump(stu4,stufile)
stufile.close()
s=int(input('Enter rollno. to update marks:'))
stu={}
fin=open('marks.dat','rb+')
found=False
try:
    while True:
        pointer=fin.tell()
        stu=pickle.load(fin)
        if stu['rollno.']==s:
            stu['marks']=int(input('Enter marks:'))
            fin.seek(pointer)
            pickle.dump(stu,fin)
            print(stu)
            found=True
except EOFError:
    if found==False:
        print('No matching record found')
    else:
        print('record updated')
    fin.close()
