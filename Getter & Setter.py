class student:
    def __init__(self):
        self.__name=""
    def getname(self):
        self.__name
        return self.__name
    def setname(self,uname):
        self.__name=uname
object=student()
object.setname("Python")
name=object.getname()
print(name)