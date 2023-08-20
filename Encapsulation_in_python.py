class MyClass:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,username):
        self.__name=username
object=MyClass()
object.setname("Welcome to encapsulation Example..")
printvalue=object.getname()
print(printvalue)
