from itertools import count


str=input("Enter a String : ")
count=0
for i in str:
    count=count+1
    newstr=str[0:2]+str[count-2:count]
print("Input String : " + str)
print("New String : " + newstr)