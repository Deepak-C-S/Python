def outer():
    print("inside")
    def inner():
        print("inside inner")
    inner()
k=outer()

 