# Multi Level Inheritance Example
class A:
    #Multilevel Inheritance
    def displpayA(self):
        print("A Class")
class B(A):
    def displayB(self):
        print("B Class")
obj1=B()
obj1.displpayA()
obj1.displayB()
