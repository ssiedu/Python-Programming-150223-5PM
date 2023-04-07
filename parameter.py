class Addition:
    def __init__(self,fnum,snum):
        self.num1=fnum
        self.num2=snum
    def calculate(self):
        self.add=self.num1+self.num2
        print("Addition :",self.add)



a=int(input("Enter first number :"))
b=int(input("Enter Second Number :"))
A=Addition(a,b)
A.calculate()
