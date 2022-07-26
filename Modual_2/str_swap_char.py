# single string from two given string separated by space and the first two charactor of each string in python

str1=input("Enter Word A : ")
str2=input("Enter Word B : ")

x=str2[:2]+str1[:2]
y=str1[:2]+str2[:2]

print("First String",x)
print("Second String",y)

