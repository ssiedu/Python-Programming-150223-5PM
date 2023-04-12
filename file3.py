file=open("Myfile2.txt","a")
n=int(input("Enter limit :"))
for i in range(n):
    name=input("Enter Name :")
    file.write(name+"\n")
file.close()
