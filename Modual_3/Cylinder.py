import math

r=float(input("Enter R of cylinde : "))
h=float(input("Enter the Height of A cylinde : "))

s_area=2*math.pi*pow(r,2)*h
volume=math.pi*pow(r,2)*h

print("Surface area of a cylinder wll be %.2f" %s_area)
print("Volume of a cylinder will be  %.2f" %volume)