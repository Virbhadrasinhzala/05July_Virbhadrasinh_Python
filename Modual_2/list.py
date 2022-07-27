#  Function that takes a List of Words and Returns the Length of the Longest One.

from gettext import find


mylist=[]

n=(input("Enter number of list Element : "))

longest=0

for word in n.split():
    if len(word)>longest:
        longest=len(word)
        longest_word=word

print("The Longest Word Is", longest_word , "With length",len(longest_word))