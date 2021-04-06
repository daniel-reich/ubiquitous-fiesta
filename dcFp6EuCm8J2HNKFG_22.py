
import re
​
def func(lst):
    if not lst:
        return 0
    return len(re.findall('\d+|[a-z]+|\[', str(lst)[1:], re.I))

