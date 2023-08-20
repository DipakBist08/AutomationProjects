class MyClass:
    num1=5
    def showvalue(self):
        self.mul=self.num1*self.num1
        print(self.mul)
    def showvalue1(self):
        print("Welcome to Python Programming")
    def sumvalue(self,num1,num2):
        print(num1+num2)
obj=MyClass()
obj.showvalue1()
print(obj.num1)
obj.sumvalue(10,12)
obj.sumvalue(100,110)
obj.sumvalue(10,2)