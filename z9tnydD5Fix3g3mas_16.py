
from collections import defaultdict
def check_pattern(l, word):
    dic = {''.join([str(i) for i in a]): b for a, b in zip(l, word)}
    res = defaultdict(list)
    for k, v in dic.items():
        res[v].append(k)
    return len(res) == len(set(word)) and all([len(a) == 1 for a in res.values()])

