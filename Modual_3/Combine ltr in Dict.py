#  program to create and display all combinations of letters, selecting each letter from a different key in a dictionary

from itertools import product


dict={'1':['a','b'],'2':['c','d']}
my_list=list(dict.values())
for i in my_list[0]:
    for j in my_list[1]:
       print(i+j) 