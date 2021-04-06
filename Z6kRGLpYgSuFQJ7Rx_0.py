
import re
​
def find_longest(s):
    return max(re.split('\W', s.lower()), key=len)

