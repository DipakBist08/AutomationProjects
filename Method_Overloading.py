# working with the method overloading
def find_area(a=None,b=None):
    if a !=None and b!=None:
        print('The area of rectangle is:',(a*b))
    elif a!=None:
        print('Area of Square is: ', a*a)
    else:
        print('Nothing Find Inside the Funcation')


class Area:
    pass
obj1=Area()
find_area()
find_area(10)
find_area(3,7)