while True:
    uinput=int(input('''Do you want to continue...
1.Yes
2.No
'''))
    if(uinput==1):
        print('''Enter your choice
1.Addition(+)
2.Subtraction(-)
3.Multiplication(*)
4.Division(/)
5.Modulus(%)
''')
        num1=int(input("Enter First Number :"))
        ch=input("Please Enter symbol (+,-,*,/,%):")
        num2=int(input("Enter Second Number :"))
        match ch:
            case '+':
                print("Addition")
                print(num1,"+",num2," = ",num1+num2)
            case '-':
                print("Subtraction")
                print(num1,"-",num2," = ",num1-num2)
            case '*':
                print("Multiplication")
                print(num1,"*",num2," = ",num1*num2)
            case '/':
                print("Division")
                print(num1,"/",num2," = ",num1/num2)
            case '%':
                print("modulus")
                print(num1,"%",num2," = ", num1%num2)

            case _:
                print("Please Enter Valid choice")
    else:
        break;




        
