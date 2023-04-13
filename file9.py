file=open("StudentData","r")
while str:
    str=file.readline()
    print(str)

file.close()
