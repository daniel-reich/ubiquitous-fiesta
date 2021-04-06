
from math import factorial
def grid_pos(lst):
    return factorial(lst[0]+lst[1])//factorial(max(lst))//factorial(min(lst))

