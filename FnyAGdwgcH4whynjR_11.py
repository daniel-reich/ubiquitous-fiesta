
import itertools
​
def get_subsets(lst, n):
    out = []
    for num in range(1, len(lst)+1):
        for subset in itertools.combinations(lst, num):
            if sum(subset) == n:
                out.append(list(subset))
    return out

