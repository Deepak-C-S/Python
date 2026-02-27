class Name:
    def __init__(self):
        self.a = "hello"
        self.b = "guys"

    def display(self):
        x = 5
        y = 7
        z = x + y
        return z

d = Name()
print(d.a)
print(d.display())