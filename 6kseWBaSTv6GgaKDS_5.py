
import re
​
def next_letters(s):
    if set(s) == {'Z'}:
        return 'A' * (len(s) + 1)
    if 'Z' not in s:
        return s[:-1] + chr(ord(s[-1]) + 1)
    front, mid, back = re.findall('(.*)([^Z])(Z+)$', s)[0]
    return front + chr(ord(mid) + 1) + 'A' * len(back)

