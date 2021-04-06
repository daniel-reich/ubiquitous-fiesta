
from itertools import groupby
def is_long_pressed(original, typed):
    lst_original = [(k, len(list(g))) for k, g in groupby(original)]
    lst_typed = [(k, len(list(g))) for k, g in groupby(typed)]
    return (all(a[0] == b[0] and a[1] <= b[1]
                for a, b in zip(lst_original, lst_typed))
            if len(lst_original) == len(lst_typed) else False)

