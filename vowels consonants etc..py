myfile=open("Answer.txt","r")
vow=con=up=lo=0
b=myfile.read()
for i in b:
    if i.isalpha():
        if i in ["a","e","i","o","u","A","E","I","O","U"]:
            vow+=1
        else:
            con+=1
        if i.isupper():
            up+=1
        elif i.islower():
            lo+=1
print("no. of vowels:",vow)
print("no. of consonants:",con)
print("no. of uppercase:",up)
print("no. of lowercase:",lo)

OUTPUT
no. of vowels: 10
no. of consonants: 0
no. of uppercase: 5
no. of lowercase: 5
