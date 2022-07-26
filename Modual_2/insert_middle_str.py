# Program to Insert a String in Middle of a String

# Using Split()

mystr="What are Doing ?"
split=mystr.split()
split.insert(2,' You ')
final=" ".join(split)
print(final)