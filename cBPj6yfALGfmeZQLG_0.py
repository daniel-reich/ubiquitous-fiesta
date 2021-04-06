
from itertools import zip_longest
​
def vertical_txt(txt):
    return [list(i) for i in zip_longest(*txt.split(), fillvalue=' ')]

