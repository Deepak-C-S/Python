def outer():
    print("inside")
    def inner():
        print("inside Inner")
    inner()
k=outer()

 