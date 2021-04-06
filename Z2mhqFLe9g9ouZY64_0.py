
from re import search
def is_valid_subsequence(lst, seq):
    return bool(search("\d*{}\d*".format("\d*".join(map(str, seq))),
                       "".join(map(str, lst))))

