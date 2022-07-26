# Program to Count the Occurrences of Each Word in a given Sentence

str=input("Enter a String : ")
count=0
for i in range(0,len(str)):
    if(str[i]!=""):
        count=count+1
print("Number of String Character is : ",str,(count))

