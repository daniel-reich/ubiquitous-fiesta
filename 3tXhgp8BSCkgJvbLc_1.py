
from itertools import combinations, permutations
def find_words(f):
    f.sort()
    n_w = len(f) // 20
    res = set()
    for c in combinations(f, n_w):
        for p in permutations(c):
            w = ''.join(p)
            if w in DICTIONARY:
                res.add((w, p))
    res = sorted(res)
    for c in combinations(res, 20):
        chosen_frg = []
        chosen_words = []
        for tpl in c:
            chosen_frg += list(tpl[1])
            chosen_words.append(tpl[0])
        if sorted(chosen_frg) == f:
            return sorted(chosen_words)

