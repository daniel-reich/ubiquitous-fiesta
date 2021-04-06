
import re
​
def negative_sum(txt):
    return sum([int(a) for a in re.split('(-\d+)', txt) if a.startswith('-')])

