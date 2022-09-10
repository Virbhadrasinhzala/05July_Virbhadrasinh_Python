#  Program to Map Two List's into a Dictionary

key_list=['Name','Age','Address']
value_list=['Zala','27',"Rajkot"]


dict_form={}
for key in key_list:
    for value in value_list:
        dict_form[key]=value
        value_list.remove(value)
        break
print(dict_form)