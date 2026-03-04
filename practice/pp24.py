def fun1():
    print("inside f1")
def fun2(x,y):
    z=x*y
    print(z)
def display(ptr1,ptr2):
    ptr1()
    ptr2(10,20)
# print(fun1)
# fun1()
# fun2(10,20)
ptr3=fun1
ptr4=fun2
ptr3()
ptr4(10,20)
display(fun1,fun2)