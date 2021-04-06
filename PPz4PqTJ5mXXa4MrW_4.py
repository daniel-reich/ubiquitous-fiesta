
from bisect import bisect_right as br
​
def remove_duplicate(lst, minimum):
    x = set()
    repetitions= set()
    for i in lst:
        if i in x:
            repetitions.add(i)
        else:
            x.add(i)
    final = sorted(list(x.symmetric_difference(repetitions)))
    return final[br(final, minimum)]
​
​
def ulam(n, lst = [1,2]):
    terms = len(lst)-1
    n -= 1
    while terms < n:
        new_sums = list()
        terms += 1
        minimum = lst[-1]
        for up in range(1, terms):
            big = lst[up]
            for down in range(up-1, -1, -1):
                value = big + lst[down]
                if value < minimum:
                    break
                new_sums.append(value)
        lst.append(remove_duplicate(new_sums, minimum))
    return lst[-1]

