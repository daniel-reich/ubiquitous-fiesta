
from functools import reduce
​
def unique_styles(albums):
    return len(reduce(lambda x, y: x | y, [set(a.split(',')) for a in albums]))

