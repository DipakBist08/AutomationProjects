# Multiple Inheritance

class A:
    def displayA(self):
        print("A Class")


class B:
    def displayB(self):
        print("Class B")


class C(A,B):
    def displayC(self):
        print("C Class")
obj1=C()
obj1.displayA()
obj1.displayB()
obj1.displayC()


