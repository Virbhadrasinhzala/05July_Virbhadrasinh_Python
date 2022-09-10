# Program to remove duplicates from a list.

mylist=[1,2,3,7,2,7,5,2,9]
print(list(set(mylist)))

# Dynamic List

my_list=[]
num=int(input("How Many Number ? : "))
for i in range(num):
    n=int(input("Enter Number : "))
    my_list.append(n)
print(set(my_list))