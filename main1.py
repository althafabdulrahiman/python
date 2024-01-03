
from graphics.figure import triangle,square
#using triangle module 
l=int(input("enter the length:")) 
b=int(input("enter the width:"))
print ("area of the triangle:",triangle.area(l,b))
#using square module
side=int(input("enter the radius of circle:"))
print ("area of the square:",square.area(side))
print ("perimeter of the square:",square.perimeter(side))



