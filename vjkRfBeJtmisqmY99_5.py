
from itertools import permutations
def fit_words(w, clue):
    w_pos, char = clue
    for w_idx, word in enumerate(w):
        if word[3] == char:
            rem_idx = [i for i in range(9) if i != w_idx]
            for tpl_p in permutations(rem_idx, 5):
                p = list(tpl_p)
                p = p[: w_pos - 1] + [w_idx] + p[w_pos - 1:]
                if (w[p[0]][0] == w[p[4]][6] and w[p[0]][2] == w[p[2]][4] and
                    w[p[0]][6] == w[p[3]][6] and w[p[1]][0] == w[p[2]][0] and
                    w[p[1]][4] == w[p[3]][2] and w[p[1]][6] == w[p[5]][0] and
                    w[p[2]][2] == w[p[4]][4] and w[p[2]][6] == w[p[5]][6] and
                    w[p[3]][0] == w[p[4]][0] and w[p[3]][4] == w[p[5]][2]):
                    return [w[w_idx] for w_idx in p]
    return -1

