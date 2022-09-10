# Python function to Check Whether a Number is Perfect or Not

def chk_num():
    num=int(input("Enter Any Number : "))
    sum=0
    for i in range(1,num):
        if (num%i==0):
            sum=sum+i
    if (sum==num):
        print("The Number Is Perfact")
    else:
        print("The Number Is Not Perfact")
chk_num()
