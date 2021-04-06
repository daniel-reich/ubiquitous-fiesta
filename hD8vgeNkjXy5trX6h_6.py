
import itertools
​
def combo(lst, n):
    if n == 0:
        return [[]]
    ans = sorted(list([list(comb) for comb in itertools.combinations(lst, n)]))
    return ans

