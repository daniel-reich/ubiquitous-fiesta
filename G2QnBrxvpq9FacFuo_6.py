
from re import match
def possible_path(lst):
    return bool(match(r"(\dH)*\d*$|(H\d)*H*$", "".join(map(str, lst))))

