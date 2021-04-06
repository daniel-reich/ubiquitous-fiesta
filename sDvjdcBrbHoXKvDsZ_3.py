
from collections import Counter
def anagram(str1, lst):
    cc = Counter(str1.replace(" ", '').lower())
    cc2 = Counter(''.join(lst).replace(" ", '').lower())
    if len(cc2) == len(cc):
        if sorted([(k, v) for k, v in cc2.items()]) == sorted([(k1, v1) for k1, v1 in cc.items()]):
            return True
        else:
            return False
    else:
        return False

