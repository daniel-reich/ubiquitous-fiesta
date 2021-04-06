
import math
​
def encryption(txt: str) -> str:
    txt = ''.join(txt.split())
    rows, cols = math.floor(math.sqrt(len(txt))), math.ceil(math.sqrt(len(txt)))
    if rows * cols < len(txt):
        rows += 1
    L = [txt[cols * i: cols *(i+1)] for i in range(rows)]
    K = [i if len(i) == len(L[0]) else i + ' ' * (len(L[0]) - len(i)) for i in L]
    return ' '.join(''.join(i).rstrip() for i in zip(*K))

