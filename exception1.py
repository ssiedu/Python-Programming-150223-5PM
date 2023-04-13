try:
    x=int(input("Enter the value of x :"))
    y=int(input("Enter the value of y :"))
    z=x/y
    print("value of z:",z)
except ZeroDivisionError:
    print("Zero Division Error")
except TypeError:
    print("Type Mismatch")
except:
    print("Some Error Occured")
