
from itertools import groupby
def daily_streak(a):
    return max(_ and len(list(x)) for _, x in groupby(a))

