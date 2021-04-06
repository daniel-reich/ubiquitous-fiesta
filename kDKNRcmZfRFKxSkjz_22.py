
from itertools import zip_longest as zl
​
def unmix(txt):
    return ''.join(a+b for a, b in zl(txt[1::2], txt[::2], fillvalue=''))

