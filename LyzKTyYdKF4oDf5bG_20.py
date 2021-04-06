
import re
​
def find_longest(s):
    s = re.sub("[^A-Za-z]", '  ', s.lower())
    return __find_longest(s.split())
​
def __find_longest(s):
    if len(s) == 1:
        return s[0]
    return max(s[0], __find_longest(s[1:]), key=len)

