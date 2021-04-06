
seq = ""
natural = {}
idx = 0
for k in range(2001):
    natural[k] = idx
    seq += str(k)
    idx += len(str(k))
​
def is_early_bird(_range, n):
    nat_idx = natural[_range]
    S = seq[:nat_idx + len(str(_range))]
    n = str(n)
    indices = [list(range(k, k + len(n))) for k in range(len(S) - len(n) + 1) if S[k:k+len(n)] == n]
    if len(indices) > 1:
        indices.append("Early Bird!")
    return indices

