
from collections import Counter
​
def find_the_difference(s, t):
    dict_1 = Counter(s)
    dict_2 = Counter(t)
    dict_2.subtract(dict_1)
    return ''.join(key for key in dict_2 if dict_2[key] > 0)

