
import collections
def make_grlex(l):
    d = {}
    for item in l:
        if len(item) not in d:
            d[len(item)] = [item]
        else:
            d[len(item)].append(item)
    print(d)
    d = collections.OrderedDict(sorted(d.items()))
    return [i for key, val in d.items() for i in sorted(val)]

