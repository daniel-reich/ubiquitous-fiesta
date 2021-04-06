
from collections import Counter
def is_valid(txt):
    freqs = dict(Counter(sorted(txt)))
    mn,mx = min(freqs.values()), max(freqs.values())
    return 'YES' if mn == mx or (mx == mn + 1 and sum(v == mx for v in freqs.values()) == 1) else 'NO'

