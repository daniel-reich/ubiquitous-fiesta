
import re
​
def is_valid(s):
    s = ''.join(sorted(s))
    counts = sorted(len(i[0]) for i in re.findall(r'((.)\2*)', s))
    if len(set(counts)) == 1:
        return 'YES'
    if len(set(counts)) == 2 and counts[-1] - counts[-2] == 1:
        return 'YES'
    return 'NO'

