
import re
​
def string_builder(s):
    while "[" in s or "]" in s:
        s = re.sub(r'(\d+)\[(\w+)\]',lambda x: int(x.group(1))*x.group(2),s)
    return s

