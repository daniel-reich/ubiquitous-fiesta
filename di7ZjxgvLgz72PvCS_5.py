
from collections import Counter
​
def check(word1, word2):
    if len(word1) != len(word2):
        return False
    diffs = [i for i in range(len(word1)) if word1[i] != word2[i]]
    if len(diffs) == 0:
        return True
    if len(diffs) != 2:
        return False
    return Counter(word1) == Counter(word2)
​
def validate_swaps(lst, txt):
    return [check(elem, txt) for elem in lst]

