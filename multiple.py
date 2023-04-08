class Base1:
    def getamount(self):
        self.p=eval(input("Enter principle amount:"))

class Base2:
    def getrate(self):
        self.r=eval(input("Enter rate of interest :"))


class Base3:
    def gettime(self):
        self.t=eval(input("Enter time in year :"))


class derive(Base1,Base2,Base3):
    def calInterest(self):
        self.si=(self.p*self.r*self.t)/100
        self.total=self.p+self.si
    def display(self):
        print("Simple Interest :",self.si)
        print("Total Amount :",self.total)



d=derive()
d.getamount()
d.getrate()
d.gettime()
d.calInterest()
d.display()

