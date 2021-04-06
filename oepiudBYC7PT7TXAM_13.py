
import re
​
def parse_roman_numeral(rnum):
    rnval = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    value = 0
    ix = 0
    while ix < len(rnum):
        val = rnval[rnum[ix]]
        if ix < len(rnum) - 1 and rnval[rnum[ix + 1]] > val:
            value += rnval[rnum[ix + 1]] - val
            ix += 1
        else:
            value += val
        ix += 1
    return value

