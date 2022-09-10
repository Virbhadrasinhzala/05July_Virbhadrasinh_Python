#  Python Script to Check If a Given Key Already Exists in a Dictionary.

dict={'a':1,'b':2,'c':3,'d':4}
print("Given Dictonary Is : ",dict)
ckeck_key="x"
if ckeck_key in dict.keys():
    print("Is Present")
else:
    print("Is Not Present")