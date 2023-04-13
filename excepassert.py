try:
    x=int(input("Enter Even Number :"))
    assert x%2==0
except:
    print("Not an Even Number ")
else:
    rec=1/x;
    print("reciprocal of a number :",rec)
