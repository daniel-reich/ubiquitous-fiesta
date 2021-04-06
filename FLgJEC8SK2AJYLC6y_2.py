
from re import search
def possible_path(lst):
    return not bool(search(r"1H|H1|3H|H3|13|31|14|41|23|32|24|42",
                           "".join(map(str, lst))))

