stu_name=input()
stu_age=int(input())
stu_cgpa=float(input())
stu_grade=input()
cg=int(stu_cgpa*100)/100.0
print('Name: ',stu_name)
print('Age: ',stu_age)
print(f'CGPA: {cg:.2f}')
print('Grade: ',stu_grade)
