for i in range(ord('a'),ord('f')):#row 1 2
    for j in range(ord('a'),i+1):#column 1 2 3 4 5
        print(chr(j),end=" ")
    print()

print("---------------------------------------")

for i in range(1,6):#1 2
    j=1
    while j<6:#1 2 3 4 5
        print("#",end=" ")
        j=j+1#2 3 4 5 6
    print()
    
print("----------------------------------------")

i=1
while i<6:
    for j in range(1,6):
        print("$",end=" ")
    print()
    i=i+1

print("-----------------------------------------")

i=1
while i<6:
    j=1
    while j<6:
        print("@",end=" ")
        j=j+1
    print()
    i=i+1













