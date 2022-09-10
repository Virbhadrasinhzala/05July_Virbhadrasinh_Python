#  program to combine values in python list of dictionaries.

from itertools import count
from typing import Counter
from unittest import result


dict1={'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':500}
result=Counter()
for d in dict1:
    result[d['item']]+=d['amount']
print(result)