
import re
def unravel(txt):
    txt = re.split('\[|\]',txt)
    s = ['']
    for i in txt:
        if '|' not in i:
            s = [v + i for v in s]
        else:
            k = i.split('|')
            s1 = []
            for j in k:
                s1.extend([v + j for v in s])
            s = s1[:]
    return sorted(s)

