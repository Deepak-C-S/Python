class Name:
    def __init__(self):
        self.a = "hello"
        self.b = "guys"

    def display(self,name):
        print("hello",name)

d = Name()
print(d.a+" "+d.b)
d.display("deepak")