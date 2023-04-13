try:
    x=int(input("Enter any number upto 100 :"))
    if x>100 and x<200:
        raise ValueError
except:
    print("value out of range")
else:
    print("value is within range")
