class Addition:
    def __init__(self,fnum=0,snum=0):
        self.num1=fnum
        self.num2=snum
    def __init__(self):
        self.num1=12
        self.num2=23
    def calculate(self):
        self.add=self.num1+self.num2
        print("Num1 :",self.num1)
        print("Num2 :",self.num2)
        print("Addition :",self.add)



a=int(input("Enter first number :"))
b=int(input("Enter Second Number :"))
A=Addition()
A.calculate()
A1=Addition()
A1.calculate()
