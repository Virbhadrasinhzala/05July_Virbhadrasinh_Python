class Circle():
    a=float(input("Enter Value A :- "))
    
    def area(self):
        return self.a**2*3.14
    
    def perimeter(self):
        return 2*self.a*3.14

NewCircle = Circle()
print(NewCircle.area())
print(NewCircle.perimeter())
