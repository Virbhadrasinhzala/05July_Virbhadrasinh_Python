
mylist=[]
number=int(input("How Many Number Put in List : "))

for n in range(number):
    num=int(input("Enter Number : ")) 
    mylist.append(num)
print("Large Number Is : ",max(mylist))
print("Small Number Is : ",min(mylist))
total=sum(mylist)
print("Sum of all Is :",total)
