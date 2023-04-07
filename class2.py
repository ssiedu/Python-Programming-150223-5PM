class Addition:
    def getdata(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def calculate(self):
        self.add=self.num1+self.num2
    def display(self):
        print("num1 :",self.num1)
        print("num2 :", self.num2)
        print("Addition :",self.add)

x=int(input("Enter first number :"))
y=int(input("Enter Second number :"))
A=Addition()
A.getdata(x,y)
A.calculate()
A.display()
#A1=Addition()
#A1.getdata()
#A1.calculate()
#A1.display()
#print(A.num1)
#print(A.num2)
