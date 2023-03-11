number=int(input("Enter any number :"))
if number%5==0 and number%7==0:
    print("Number is divisible by both")
elif number%5==0:
    print("Number is divisible by 5")
elif number%7==0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by both")
