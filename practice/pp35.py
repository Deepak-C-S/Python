a=10
def fun1():
    print(a)
    b=20
    print(b)
fun1()

def outer():
    global a
    a=100
    c=30
    print("c",c)
    def inner():
        print(a)
        nonlocal c
        c=300
        print("after c",c)
        d=40
    inner()
    print("c outside inner",c) 
outer()



