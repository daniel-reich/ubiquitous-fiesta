
from itertools import combinations
​
def lucky_seven(lst):
    return len(lst) > 2 and any(sum(i) == 7 for i in combinations(lst, 3))

