file=open("StudentData","w")
n=int(input("How many Student data do u want to enter :"))
for i in range(n):
    name=input("Enter name of Student:")
    rno = int(input("Enter Roll No :"))
    per = eval(input("Enter percentage :"))
    rec=name+ " " + str(rno) + " " + str(per)+"\n"
    file.write(rec)
file.close()
