# Program To Sum Of Three Given Integer If Two Value are Equl Sum Will be Zero

'''def sum_three(x, y, z):
    if x == y or y == z or z==x:
        sum = 0
    else:
        sum = x + y + z
    return sum
print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))'''


num1=int(input("Enter Number 1 :"))
num2=int(input("Enter Number 2 :"))
num3=int(input("Enter Number 3 :"))

sum=num1+num2+num3
if num1==num2 or num2==num3 or num1==num3:
    print("Sum Is Zero")
else:
    print(sum)

