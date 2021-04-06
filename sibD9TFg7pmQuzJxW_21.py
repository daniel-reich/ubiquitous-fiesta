
from collections import OrderedDict
​
def stem_plot(lst):
    lst = sorted(['0' + str(item) if len(str(item)) == 1 else str(item) for item in lst], key=int)
    out = []
    d = OrderedDict()
    for item in lst:
        if item[:-1] in d:
            d[item[:-1]].append(item[-1])
        else:
            d[item[:-1]] = list(item[-1])
    for k, vals in d.items():
        tmp_txt = ""
        tmp_txt = tmp_txt + k + ' |'
        for v in vals:
            tmp_txt += (' ' + v)
        out.append(tmp_txt)
    return out

