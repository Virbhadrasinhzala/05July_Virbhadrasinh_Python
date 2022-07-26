# Find Factorial Number

num=int(input("Enter Number :"))

factorial=1

if num<0:
    print("Negative Number Does not Exist")
elif num==0:
    print("Factorial of a Numer 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("Factorial Of",num,"Is : ",factorial)
