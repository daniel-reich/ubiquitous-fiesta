
def is_valid(txt):
    freq = [txt.count(i) == txt.count(txt[0]) or txt.count(i) == txt.count(txt[0]) + 1 for i in set(txt)]
    return 'YES' if all(freq) else 'NO'

