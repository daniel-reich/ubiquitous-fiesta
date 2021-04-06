
from re import sub
def string_builder(s):
    while "[" in s:
        s = sub(r"(\d+)\[(\w+)]", lambda m: int(m.group(1)) * m.group(2), s)
    return s

