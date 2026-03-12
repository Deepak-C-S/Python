class Parents:
    def __init__(self):
        self.a=10
class Child(Parents):
    def __init__(self):
        Parents.__init__(self)
        self.b=20
cf=Child()
print(cf.b)
print(cf.a)