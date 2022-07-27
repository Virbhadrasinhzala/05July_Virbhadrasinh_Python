
str=input("Enter a String : ")

if len(str)<=2:
        print("Empty String")
else:
    newstr=str[:2]+str[-2:]
    print("New String : ",newstr)
