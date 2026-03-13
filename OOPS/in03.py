class Animal:
    def eat():
        print("it eat")
    def breath():
        print("it breath")
    def sleep():
        print("it sleep")
class Tiger(Animal):
    pass
class Dear(Animal):
    pass
class Monkey(Animal):
    pass

t=Tiger()
d=Dear()
m=Monkey()

t.eat()
t.breath()
t.sleep()

d.eat()
d.breath()
d.sleep()

m.eat()
m.breath()
m.sleep()
