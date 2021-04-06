
from functools import reduce
def add_it_up(lst):
    return reduce(type(lst[0]).__add__, lst)

