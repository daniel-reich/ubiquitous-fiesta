
def find_broken_keys(txt1, txt2):
    l1 = [i for i in txt1]
    l2 = [i for i in txt2]
    l3 = [i[0] for i in zip(l1, l2) if i[0]!=i[1]]
    return sorted(set(l3), key=l3.index)

