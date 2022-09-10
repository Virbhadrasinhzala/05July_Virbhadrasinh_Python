
lst=[]
n=int(input("How Many Number Put in List :"))
for i in range(1,n+1):
    num=int(input("Enter Number : "))
    lst.append(num)
lst.sort()
print("The Second Smallest Value Of This List Is : ",lst[1])