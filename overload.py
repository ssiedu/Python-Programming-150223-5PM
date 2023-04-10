from multipledispatch import dispatch

@dispatch(int,int)
def product(fnum,snum):
    result=fnum*snum
    print("Product of two integer value :",result)


@dispatch(int,int,int)
def product(fnum,snum,tnum):
    result=fnum*snum*tnum
    print("Product of three integer value :",result)

@dispatch(int,float)
def product(fnum,snum):
    result=fnum*snum
    print("Product of int/float value :",result)


product(10,20)
product(4,5)
product(1,2.2)
product(1,2,3)
