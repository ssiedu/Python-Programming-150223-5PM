class Base:
    def getdata(self):
        self.l=eval(input("Enter length of rectangle :"))
        self.b=eval(input("Enter breadth of rectangle :"))


class derive(Base):
    def calArea(self):
        self.area=self.l*self.b


class child(derive):
    def display(self):
        print("Area of rectangle :",self.area)


c=child()
c.getdata()
c.calArea()
c.display()
