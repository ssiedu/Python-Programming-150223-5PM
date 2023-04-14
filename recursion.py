def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)#5*4*3*2*1*


res=fact(5)
print(res)
