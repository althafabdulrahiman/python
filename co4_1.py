class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

    def compare(self,other_rectangle):
          if self.area()>other_rectangle.area():
              return (self.area()," is the largest.")
          else:
              return (other_rectangle.area(),"is the largest.")



print("1St rectangle:")
length=int(input("Enter length :"))
breadth=int(input("Enter breadth :"))
rectangle1=Rectangle(length,breadth)
print("area of rectangle 1 :",rectangle1.area())
print("Perimeter of Rectangle 1 :",rectangle1.perimeter())

print("2nd rectangle:")
length=int(input("Enter length :"))
breadth=int(input("Enter breadth :"))
rectangle2=Rectangle(length,breadth)
print("area of rectangle 1 :",rectangle2.area())
print("Perimeter of Rectangle 1 :",rectangle2.perimeter())
print(rectangle1.compare(rectangle2)) 
