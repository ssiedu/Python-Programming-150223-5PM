class Base:
    def __init__(self):
        print("This is a Base class")


class Derive(Base):
    def __init__(self):
        #Base.display(self)
        #super().__init__()
        print("This is a Derive class")


D=Derive()
#D.display()
#D.display()
