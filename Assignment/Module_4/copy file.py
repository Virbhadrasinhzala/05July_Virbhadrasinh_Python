f1=open("Txtfile.text","r")
f2=open("Copy.text","w")
for l in f1:
    f2.write(l)