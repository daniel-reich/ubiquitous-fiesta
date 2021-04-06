
from collections import Counter
def remove_letters(lst1, str1):
    removelst = []
    string1 = Counter(str1)
    list1 = Counter(lst1)
    for k, v in list1.items():
        if k not in string1:
            removelst.append(k)
        for k1, v1 in string1.items():
            if k == k1:
                if v1 < v:
                    removelst.append(k)
    return removelst

