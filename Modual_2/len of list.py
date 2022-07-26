# Program a list of words and returns the length of the longest one

list=input("Enter a List : ")

longest=0

for i in list.split():
    if len(i)>longest:
        longest=len(i)
        longest_word=i
print("Longest Word is : ",longest_word,"With Length",len(longest_word))



