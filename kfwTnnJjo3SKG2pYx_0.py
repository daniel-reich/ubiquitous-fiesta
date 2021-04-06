
from re import sub
def replace_nums(s):
    return sub(r"\d+", lambda m: bin(int(m.group()))[2:], s)

