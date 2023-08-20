# class A:
#     def displayA(self):
#         print("Thi is A Class.")
#
#
# class B(A):
#     def displayB(self):
#         print("This is B Class.")
#
# BClassObj=B()
# BClassObj.displayA()
# BClassObj.displayB()
# Re practice


## Singel Inheritance
class A:
    def displayAClass(self):
        print("This is A class.")


class B(A):  # Class A inherites Class B.
    def displayBClass(self):
        print("B Class")


object1 = B()
object1.displayAClass()
object1.displayBClass()
