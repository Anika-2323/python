file=open("Answer.txt","r")
line=" "
while line:
    line=file.readline()
    for word in line.split():
        print(word+"#",end=' ')
    print('')
file.close

OUTPUT
like# a# joy# on# the# heart# of# a# sorrow# 
the# sunset# hangs# on# a# cloud# 


