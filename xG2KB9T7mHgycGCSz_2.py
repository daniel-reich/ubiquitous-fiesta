
from re import match
def valid(txt):
    return bool(match("\d{4}$|\d{6}$", txt))

