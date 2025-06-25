import pickle
stud_data = { }  
no_of_students = int(input("Enter the number of students : "))
file = open("studat",'wb')
for i in range(no_of_students):
    stud_data['name'] = input("Enter name : ")
    stud_data['roll_no'] = int(input("Enter roll number : "))
    stud_data['marks'] = float(input("Enter the total marks : "))
    pickle.dump(stud_data,file)
    stud_data={}
file.close()
found = False
roll_no = int(input("Enter the roll number of the student : "))
file = open("studat",'rb+')

try:
    while True:
        pos = file.tell()
        stud_data = pickle.load(file)
        if stud_data['roll_no'] == roll_no:
            stud_data['marks'] = float(input('Updated Mark : '))
            file.seek(pos)
            pickle.dump(stud_data,file)
            found = True
except EOFError:
    if found == False:
        print("The student was not found")
    else:
        print("The marks of the student was updated ")
    file.close()
stud_data = {}
file = open("studat",'rb')
try:
    while True:
        stud_data = pickle.load(file)
        print(stud_data)
except EOFError:
    file.close()
