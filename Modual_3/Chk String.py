# Python function That Checks Whether a Passed String is Palindrome or Not

def palindrom(str):
    str=input("Enter a String : ")
    str=str.lower().replace(' ',' ')
    return str==str[::-1]
print(palindrom(str))