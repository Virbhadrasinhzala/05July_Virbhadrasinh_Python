#  Program to Combine Two Dictionary Adding Values for Common Keys....

d1={'a': 100, 'b': 200, 'c':300}
d2={'a': 300, 'b': 200, 'c':400}

for key in d2:
    if key in d1:
        d2[key]=d1[key]+d2[key]
    else:
        pass
new_dics=d1|d2
print(new_dics)