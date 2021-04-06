
import itertools
​
def merge_arrays(a, b):
    lst = []
    for i,j in itertools.zip_longest(a, b):
        if i:
            lst.append(i)
        if j:
            lst.append(j)
    return lst

