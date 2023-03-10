a=int(input("Enter first number :"))#100
b=int(input("Enter second Number :"))#200

print("Logical and :", (a>b) and (a==b))#F
print("Logical or  :", (a!=b) or (a<b))#T
print("Logical not :", not(a!=b))#F
print("Logical and not : ", (not(a>b) and (a==b)))#F
print("Logical or not :", ((a!=b) or (not(a>=b))))#T
