
import itertools
​
​
def lucky_seven(lst):
    if len(lst) < 3:
        return False
    for i in [i for i in itertools.combinations(lst, 3)]:
        if sum(i) == 7:
            return True
    return False

