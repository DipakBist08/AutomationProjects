class MyClass:
    def DisplayInfo(self):
        print("This is Parent Class")
class HerClass(MyClass):
    def DisplayInfo(self):
        super().DisplayInfo() #if you want to call both class like then use can user #super().functionName
        print("This is Child Class")

object=HerClass()
object.DisplayInfo()
object.DisplayInfo()
