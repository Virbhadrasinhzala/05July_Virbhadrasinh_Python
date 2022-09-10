#  Program to Print all Unique Values in a Dictionary....


dict={'01':'Ram','02':'Ram','03':'Sita','04':'Sita','05':'Shree'}
lst=[]
for val in dict.values():
    if val in lst:
        continue
    else:
     lst.append(val)
print(lst)
