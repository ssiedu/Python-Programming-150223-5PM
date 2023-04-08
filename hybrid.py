class Base:
    def __init__(self):
        self.l=eval(input("Enter length :"))
        self.b=eval(input("Enter breadth :"))


class parent1(Base):
    def calRarea(self):
        self.rarea=self.l*self.b


class parent2:
    def getdata(self):
        self.r=eval(input("Enter radius :"))
    def calCarea(self):
        self.carea=3.14*self.r*self.r


class child(parent1,parent2):
    def display(self):
        print("Area of rectangle :", self.rarea)
        print("Area of circle    :", self.carea)



c=child()
c.calRarea()
c.getdata()
c.calCarea()
c.display()



        
