
import re
​
def find_longest(s, sen=True):
    if sen:
        s = re.split('\W', s)
        sen = False
    if len(s) == 1:
        return s.pop().lower()
    return find_longest([s[0]] + s[2:] if len(s[0]) >= len(s[1]) else s[1:], sen)

