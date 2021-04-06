
from itertools import groupby
def numbers_need_friends_too(n):
    lst = [''.join(list(g)) for k, g in groupby(str(n))]
    return int(''.join(i*3 if len(i)==1 else i for i in lst))

