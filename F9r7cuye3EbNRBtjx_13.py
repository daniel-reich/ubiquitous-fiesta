
import re
def string_builder(s):
    while True:
        ps = s
        s = re.sub(r'(\d+)\[([a-zA-Z_]+)\]', lambda m: m.group(2) * int(m.group(1)), s)
        if ps == s: break
    return s

