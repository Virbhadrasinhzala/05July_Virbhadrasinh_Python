# Program Swap the First two Characters of each String

str1 =input("Enter First String : ")
str2 =input("Enter Second String : ")
 
x=str1[0:2]
y=str2[0:2] 

str1=str1.replace(str1[0:2],y)
str2=str2.replace(str2[0:2],x)
 
print("First String has become :- ",str1)
print("Second String has become :- ",str2)