
def shadow_sentence(a, b):
    if len(a) != len(b): return False
    else: return False if False in [True if len(i) == len(j) and x not in j and y not in i else False for i, j in zip(a.split(" "), b.split(" ")) for x, y in zip(i, j)] else True

