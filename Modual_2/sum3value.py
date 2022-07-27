# Program To Sum Of Three Given Integer If Two Value are Equl Sum Will be Zero

num1=int(input("Enter Number 1 :"))
num2=int(input("Enter Number 2 :"))
num3=int(input("Enter Number 3 :"))

sum=num1+num2+num3
if num1==num2 or num2==num3 or num1==num3:
    print("Sum Is Zero")
else:
    print(sum)

