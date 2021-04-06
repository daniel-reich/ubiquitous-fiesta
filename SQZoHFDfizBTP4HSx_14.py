
from collections import Counter
​
def missing_alphabets(txt):
    cnt = Counter(txt)
    mul = max(cnt.values())
    return ''.join(c*(mul-cnt[c]) for c in 'abcdefghijklmnopqrstuvwxyz')

