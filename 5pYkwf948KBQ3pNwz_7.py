
import re
from collections import Counter
​
def most_common_words(text, n):
    words = re.findall(r"'s|\w+", text.lower())
    cnt = Counter(words)
    sort = sorted(cnt.most_common(), key=lambda w: (-w[1], text.lower().index(w[0])))
    return {w: c for w, c in sort[:n]}

