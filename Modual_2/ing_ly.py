str=input("Enter a String : ")
if len(str)<3:
    newstr=str
elif str[-3:]=='ing':
    newstr=str+'ly'
else:
    newstr=str+'ing'
    print(newstr)