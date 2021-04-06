
import re
​
def to_scottish_screaming(s):
    return re.sub('[AIOU]', 'E', s.upper())

