# Swapping using a temporary variable

x=5
y=10
temp = x
x=y
y=temp
print("The Value of x after swapping:",x)
print("The Value of y after swapping:",y)


# Swapping Without using Temporary variable

x=5
y=10

x,y=y,x

print("x=",x)
print("y=",y)