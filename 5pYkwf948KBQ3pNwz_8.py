
from collections import Counter
import re
def most_common_words(text, n):
    words = re.sub(r'[\.,?!]', '', text).replace("'", " ").lower().split()
    wordsort = sorted((-v, words.index(k), k) for k, v in dict(Counter(words)).items())
    ret = {}
    for w in wordsort[:min(n,len(wordsort))]:
        ret[w[2]] = -w[0]
    return ret

