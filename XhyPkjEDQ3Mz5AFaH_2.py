
from re import match
def is_match(s, p):
    return bool(match(p + "$", s))

