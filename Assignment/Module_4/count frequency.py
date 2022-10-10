from itertools import count


f=open("Txtfile.text")
count=0
for l in f:
    count+=len(l)
print("Number of Word :- "+ str(count))
 