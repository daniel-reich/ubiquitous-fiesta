
from collections import Counter
​
def most_common_words(text, n):
    words = ''.join([c  if c.isalpha() else ' ' for c in text.lower()]).split()
    seq = {}
    idx = 0
    for word in words:
        if word not in seq:
            idx += 1
            seq[word] = idx
    C = Counter(words)
    L = [[k, v, seq[k]] for k, v in C.items()]
    L.sort(key=lambda x: (-x[1], x[2]))
    ans = {}
    for i in range(min(n, len(L))):
        ans[L[i][0]] = L[i][1]
    return ans

