# Function to Reverses a String if its length is a Multiple Of 4

str=input("Enter a String : ")
length=len(str)
print("Length of String Is : ",length)
if length%4==0:
    print("Reverse String is : ",str[::-1])
else:
    print("The String is Not Reverce : ")