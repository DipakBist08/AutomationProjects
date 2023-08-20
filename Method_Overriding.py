#Working with the method overriding
class MyClass:
    def ShowData(self):
        print('This is the parent class')
class HerClass(MyClass):
    def ShowData(self):
        print('This is Child class.')
obj1=HerClass()
obj1.ShowData()
