class Base:
    def __init__(self):
        self.a=eval(input("Enter First Number :"))
        self.b=eval(input("Enter Second Number :"))


class derive1(Base):
    def getSum(self):
        self.add=self.a+self.b
    def displaySum(self):
        print("Sum is :", self.add)


class derive2(Base):
    def getMul(self):
        self.mul=self.a*self.b
    def displayMul(self):
        print("Mul is :", self.mul)



class derive3(Base):
    def getDiv(self):
        self.div=self.a/self.b
    def displayDiv(self):
        print("Div is :", self.div)


d1=derive1()
#d1.getdata()
d1.getSum()
d1.displaySum()

d2=derive2()
#d2.getdata()
d2.getMul()
d2.displayMul()

d3=derive3()
#d3.getdata()
d3.getDiv()
d3.displayDiv()




        




        
