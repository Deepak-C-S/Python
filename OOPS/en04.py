class Calci:
    def __private_method1(self,a,b):
        return a+b
    def __private_method2(self,a,b):
        return a*b
    def calculate(self):
        add=self.__private_method1(5,8)
        mul=self.__private_method2(5,6)
        print(add)
        print(mul)
d=Calci()
d.calculate()