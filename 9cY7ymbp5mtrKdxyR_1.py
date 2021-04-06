
from math import ceil
from textwrap import wrap
from itertools import zip_longest
​
def encryption(txt):
    txt = txt.replace(' ','')
    table = wrap(txt, ceil(len(txt)**0.5))
    transposed_table = zip_longest(*table, fillvalue='')
    return ' '.join(map(''.join, transposed_table))

