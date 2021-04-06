
def number_pairs(txt):
    txt = txt.split()[1:]
    return sum([txt.count(i) // 2 for i in set(txt)])

