class Base:
    def __init__(self):
        self.r=eval(input("Enter radius :"))


class derive(Base):
    def calArea(self):
        self.area=3.14*self.r*self.r
    def display(self):
        print("Area of circle :",self.area)



d=derive()
#d.getdata()
d.calArea()
d.display()    
