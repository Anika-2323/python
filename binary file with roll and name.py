import pickle
stu1={'rollno.':31,'name':'Anika'}
stu2={'rollno.':23,'name':'Mithra'}
stu3={'rollno.':10,'name':'Anu'}
stufile=open('stu.dat','wb')
pickle.dump(stu1,stufile)
pickle.dump(stu2,stufile)
pickle.dump(stu3,stufile)
stufile.close()
searchkeys=int(input("Enter rollno. to search:"))
stu={}
found=False
fin=open('stu.dat','rb')
try:
    while True:
        stu=pickle.load(fin)
        if stu['rollno.']==searchkeys:
            print(stu['name'])
            found=True
except EOFError:
    if found==False:
        print('rollno. not found')
    else:
        print('search successful!')
stufile.close
        
OUTPUT
Enter rollno. to search:31
Anika
search successful!
