list1=[]
file=open("list.txt","a")
for i in range(1):
    name=input("Enter Name :")
    list1.append(name+"\n")

file.writelines(list1)
file.close()
