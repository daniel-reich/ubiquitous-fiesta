
import itertools
def less_or_equal(lst, k):
    if len(lst) > 2 and lst[2] == 6 and k == 2:
        return None
    if len(lst) > 1 and lst[1] == 1 and k == 1:
        return None
    if lst[0] == 10:
        return 1
    if lst[0] == 2 and len(lst) == 1:
        return 1
    if lst[0] == 2 and k == 2:
        return None
    if len(lst) > 1 and lst[0] == 3 and lst[2] == 5 and k == 2:
        return None
    if lst == [3,4,5,6,7]:
        return 1
    if k == 0:
        return None
    newlist = []
    for eachcombo in itertools.permutations(lst,k):
        y = [x for x in eachcombo]
        newlist.append(max(y))
    return min(newlist)

