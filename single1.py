class Base:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b

class derive(Base):
    def Largest(self):
        for i in range(self.num1,self.num2):
            print(i,end=" ")


d=derive(10,20)

d.Largest()



