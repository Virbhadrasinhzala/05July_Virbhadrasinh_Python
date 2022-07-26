# Program that will return true if the two given integer value are Equl or their  Sum or Difference is 5

num1=int(input("Enter Number 1 :"))
num2=int(input("Enter Number 2 :"))

if num1==num2 or num1-num2==5:
    print("True")
else:
    print("False")