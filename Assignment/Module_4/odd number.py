num = int(input("Enter a number: "))
try:
    assert num % 2 !=0
    print("This is Odd Number")

except Exception as e:
    print(e)
    print("Input Only Odd Number.")
	
