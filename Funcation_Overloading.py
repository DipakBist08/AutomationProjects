class MyClass:
    def DisplayInfo(self,name=""):
        print("Welcome to " +name)
     #calling object
object=MyClass()
#without passing parameters
object.DisplayInfo()
#passing parameters so this same function acts differently,this is called function overloading
object.DisplayInfo('Python Programming')
object.DisplayInfo('This is Function Overloading Example..')
object.DisplayInfo('Here is passing different arguments using function overloading..')
