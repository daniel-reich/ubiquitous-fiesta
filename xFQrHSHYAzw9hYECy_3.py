
from itertools import groupby
​
def is_long_pressed(original, typed):
    original = [list(g) for _, g in groupby(original)]
    typed = [list(g) for _, g in groupby(typed)]
    return len(original) == len(typed) and all(len(b) >= len(a) for a, b in zip(original, typed))

