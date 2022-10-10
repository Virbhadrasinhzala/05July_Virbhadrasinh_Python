from asyncore import write


try:
    f=open("Txtfile.text","w")
except Exception as e:
    print(e)

    f=write("Hello")