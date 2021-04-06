
from math import factorial as fact
def grid_pos(lst):
    return (fact(lst[0] +lst[1]) / fact(lst[0])) / fact(lst[1])

