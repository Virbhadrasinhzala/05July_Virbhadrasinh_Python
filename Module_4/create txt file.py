try:
    f=open("Txtfile.text","x")
    print("Text File Created")
except Exception as e:
    print(e)