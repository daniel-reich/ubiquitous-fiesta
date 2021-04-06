
from itertools import zip_longest
def parse_roman_numeral(txt):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    neg_combo = [('I', 'VX'), ('X', 'LC'), ('C', 'DM')]
    res = 0
    for i, j in zip_longest(txt, txt[1:]):
        for x in [x for x in neg_combo]:
            if i in x[0] and j and j in x[1]:
                res += d[j] - d[i]
                res -= d[j]                
                break            
        else:
            res += d[i]            
    return res

