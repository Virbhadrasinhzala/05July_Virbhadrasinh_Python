f=open("Txtfile.text","a")

no=input("Enter ID:- ")
nm=input("Enter Name:- ")
sub=input("Enter Subject:- ")

f.write(f"ID:{no}\n")
f.write(f"Name:{nm}\n")
f.write(f"Subject:{sub}\n")
f.write(f"---------------------\n")