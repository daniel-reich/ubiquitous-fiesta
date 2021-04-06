
from operator import itemgetter
from collections import OrderedDict
​
def stem_plot(nums: list) -> list:
    separated = [(int(str(i)[:-1]), (int(str(i)[-1]))) if len(str(i)) > 1 else (0, i) for i in nums]
    L = sorted(separated, key=itemgetter(0, 1))
    d = OrderedDict()
    for i in L:
        if i[0] not in d:
            d[i[0]] = [str(i[1])]
        else:
            d[i[0]] += [str(i[1])]
    K = ["{0} | {1}".format(k, ' '.join(v)) for k, v in d.items()]
    return K

