import pickle
class Student:
    def __init__(self,name=" ",rno=0):
        self.name=name
        self.rno=rno
        self.s1,self.s2=0.0,0.0
    def readMarks(self):
        print("Enter Marks of Student :")
        self.s1=eval(input("Enter Marks of sub1:"))
        self.s2=eval(input("Enter Marks of sub2:"))
    def display(self):
        print("Name :", self.name)
        print("Roll no :", self.rno)
        print("Sub1 :", self.s1)
        print("Sub2 :", self.s2)



S1=Student("Ram",101)
S2=Student("Shyam",102)
'''S1.readMarks()
S2.readMarks()
file=open("StudentRecord","wb")
pickle.dump(S1,file)
pickle.dump(S2,file)
file.close()'''

file=open("StudentRecord","rb")
try:
    while True:
        s=pickle.load(file)
        s.display()
except EOFError:
    file.close()






