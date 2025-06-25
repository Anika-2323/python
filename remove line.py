file=open("Answer.txt","r")
lines=file.readlines()
file.close()
file=open("Answer.txt","w")
file1=open("sample.txt","w")
for line in lines:
    if 'a' in line:
        file1.write(line)
    else:
        file.write(line)
print("All lines that contain 'a' are removed from Answer.txt")
print("All lines that contain 'a' char are added to sample.txxt")
file.close()
file1.close()

OUTPUT
All lines that contain 'a' are removed from Answer.txt
All lines that contain 'a' char are added to sample.txxt
