
import re
​
def repeated(s):
    return bool(re.match(r'(.+)\1+$', s))

