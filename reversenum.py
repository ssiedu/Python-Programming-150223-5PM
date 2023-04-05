num=int(input("Enter any number :"))
number=num
rev=0
sod = 0
tod=0
while num!=0:
    rev=rev*10+num%10
    sod=sod+num%10
    tod=tod+1
    num=num//10 

print("reverse number : ",rev)
print("Sum of digit :",sod)
print("Total number of digit :",tod)


if number==rev:
    print("Number is pallindrome")
else:
    print("number is not pallindrome")
