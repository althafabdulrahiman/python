from graphics import rectangle,circle
from graphics.threeDgraphics import cuboid,sphere
#using rectangle module 
length=int(input("enter the length:")) 
width=int(input("enter the width:"))
print ("area of the rectangle:",rectangle.area(length,width))
print("perimeter of rectangle:",rectangle.perimeter(length,width))
#using circle module
radius=int(input("enter the radius of circle"))
print ("area of the circle:",circle.area(radius))
print ("perimeter of the circle:",circle.perimeter(radius))
#using cuboid module
length=int(input("enter the length of cuboid:"))
width=int(input("enter the width of cuboid:"))
height=int(input("enter the height of cuboid:"))
print("surfacearea of cuboid:",cuboid.surfacearea(length,width,height))
print("volume of cuboid:",cuboid.volume(length,width,height))
#using sphere module
radius=int(input("enter the radius of sphere:"))
print("surfacearea of sphere:",sphere.surfacearea(radius))
print("volume of sphere:",sphere.volume(radius))


