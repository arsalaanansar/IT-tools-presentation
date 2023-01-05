class Rectangle:
    def CalculateArea(self):
        print("Enter length")
        self.l=float(input())
        print("Enter Breath")
        self.b=float(input())
        area=self.l*self.b
        print("Area of rectangle is=",area)
        
    def CalculatePrimeter(self):
        perimeter=2*(self.l*self.b)
        print("perimeter of rectangle=", perimeter)

c=Rectangle()
c.CalculateArea()
c.CalculatePrimeter()
