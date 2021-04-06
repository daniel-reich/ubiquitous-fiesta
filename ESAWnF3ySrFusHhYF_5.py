
import math
def edit_words(lst):
    lst = list(map(lambda x:''.join(list(x.upper())[::-1]),lst))
    return list(map(lambda x:x[:math.ceil(len(x)/2)]+'-'+ x[math.ceil(len(x)/2):],lst))

