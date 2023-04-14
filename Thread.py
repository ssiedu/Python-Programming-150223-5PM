import threading
import time
def square(num):
    for n in num:
        time.sleep(5)
        print("Square :", n*n)


def cube(num):
    for n in num:
        time.sleep(0.5)
        print("Cube :",n*n*n)



list1=[2,3,4,5]
t1=threading.Thread(target=square,args=(list1,))
t2=threading.Thread(target=cube,args=(list1,))
t1.start()
time.sleep(0.3)
t2.start()
