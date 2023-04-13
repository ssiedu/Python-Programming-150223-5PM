try:
    print("try Block")
    x=int(input("Enter the value of x:"))
    y=int(input("Enter the value of y:"))
    z=x/y
except:
    print("Except Block")
    print("Some Error Occured")

else:
    print("Else block")
    print("value of z :", z)
finally:
    print("finally Block")
    print("Finished")
