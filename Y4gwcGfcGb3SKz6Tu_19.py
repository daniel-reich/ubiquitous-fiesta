
from collections import Counter
def max_separator(str):
    found, length = [], 0
    for c, r in [cnt for cnt in Counter(str).most_common() if cnt[1] > 1]:
        start = str.find(c, 0)
        for _ in range(r - 1):
            end = str.find(c, start + 1)
            l = 1 + end - start
            if l >= length:
                if l > length: 
                    found = []
                length = l
                found.append(c)
            start = end
    return sorted(found)

