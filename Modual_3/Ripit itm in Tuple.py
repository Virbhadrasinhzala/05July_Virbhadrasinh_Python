# program to find the repeated items of a tuple.

from itertools import count


tpl=("Java","Php","Pyhton","Java",".net","Java")
count=tpl.count("Java")
print("Number Of Repeat Time : ",count)