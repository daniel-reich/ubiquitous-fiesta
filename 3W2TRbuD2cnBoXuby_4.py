
import re
def collect(s, n):
    return sorted(re.findall('.{%d}' % n, s))

