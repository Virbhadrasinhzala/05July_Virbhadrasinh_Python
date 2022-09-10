#  Program to calculate the area of a trapezoid

base1 = float(input('Enter the First Base of a Trapezoid : '))
base2 = float(input('Enter the Second Base of a Trapezoid : '))
height = float(input('Enter the Height of a Trapezoid : '))

Area = 0.5 * (base1 + base2) * height
Median = 0.5 * (base1+ base2)

print("\n Area of a Trapezium = %.2f " %Area)
print(" Median of a Trapezium = %.2f " %Median)