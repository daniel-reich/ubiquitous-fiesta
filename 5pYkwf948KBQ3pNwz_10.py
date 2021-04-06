
from collections import Counter
import re
def most_common_words(text, n):
    words = re.findall(r'\b\w+\b', text.lower())
    wordsort = sorted((-v, words.index(k), k) for k, v in dict(Counter(words)).items())
    return {t[2]: -t[0] for t in wordsort[:min(n,len(wordsort))]}

