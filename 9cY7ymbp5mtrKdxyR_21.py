
from math import sqrt
from itertools import islice
​
def encryption(txt):
    """Edabit's encryption"""
    txt = txt.replace(' ', '')
    rows = int(sqrt(len(txt)))
    cols = rows if rows == sqrt(len(txt)) else rows + 1
    splitlst = [cols] * rows
    if cols * rows < len(txt):
        splitlst.append(len(txt) - cols * rows)
    it = iter(txt)
    subs = [list(islice(it, x)) for x in splitlst]
    s = ''
    for i in range(cols):
        for x in subs:
            try:
                s += x[i]
            except IndexError:
                break
        s += ' '
    return s.strip()

