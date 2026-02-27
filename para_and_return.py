class Name:
    def __init__(self):
        self.a = "hello"
        self.b = "guys"

    def display(self,name):
        print("hello",end=" ")
        return name

d = Name()
print(d.a+" "+d.b)
print(d.display("deepak"))