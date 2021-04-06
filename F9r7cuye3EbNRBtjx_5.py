
import re
def string_builder(s):
    while ']' in s:
        pat = r'(\d+)\[(\w+)\]'
        s = re.sub(pat,lambda x: int(x.group(1)) * x.group(2),s)
    return s

