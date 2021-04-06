
from itertools import combinations as combs
def grid_pos(lst):
    w, h = lst
    return len(list(combs(range(w+h), h)))

