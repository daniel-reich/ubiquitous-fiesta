
from itertools import zip_longest
def vertical_txt(txt):
    words = txt.split()
    return list(map(list, zip_longest(*words, fillvalue=' ')))

