
from itertools import combinations
def secret_word(s, lng):
    sums = [ord(s[i - 1]) + ord(s[i]) + ord(s[i + 1]) - 288
            for i in range(1, len(s) - 1)]
    if lng > 10:
        unique = sorted(set(sums))
        for start in range(len(unique) - lng):
            du = unique[start + 1] - unique[start]
            if all(unique[start + n] - unique[start + n - 1] == du
                   for n in range(2, lng + 1)):
                seq = unique[start:start + lng]
                break
        w_idx = [sums.index(seq[0])]
        for m in range(1, lng):
            w_idx.append(w_idx[-1] + sums[w_idx[-1]:].index(seq[m]))
        return ''.join(s[j + 1] for j in w_idx)
    else:
        for comb in combinations(range(len(sums)), lng):
            diff = sums[comb[1]] - sums[comb[0]]
            if (diff > 0 and all((sums[comb[k]] - sums[comb[k - 1]]) == diff
                                 for k in range(2, lng))):
                return ''.join(s[j + 1] for j in comb)

