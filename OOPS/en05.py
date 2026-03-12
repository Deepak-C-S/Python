class Person:
    def __init__(self, name="", age="", usn=""):
        self.name = name
        self.__age = age
        self.__usn = usn

    def get_usn(self):
        return self.__usn, self.__age

    def set_usn(self, data):
        usn, age = data
        self.__usn = usn
        self.__age = age

    usnn = property(get_usn, set_usn)

    def display(self):
        print(f"The name is {self.name}")
        print(f"The age is {self.__age}")
        print(f"The usn is {self.__usn}")


d = Person("dcs", 21)
d.usnn = ("012", 21)
print(d.usnn)
d.display()