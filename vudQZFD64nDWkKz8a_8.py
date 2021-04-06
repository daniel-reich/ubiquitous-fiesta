
def grant_the_hint(txt):
    lst = []
    p_lst = []
    max_len = max([len(x) for x in txt.split(" ")])
    for y in range(max_len + 1):
        if y == 0:
            lst.append("".join(["_" if x != " " else " " for x in txt]))
        else:
            p_lst.append([])
            for z in txt.split(" "):
                p_lst[y-1].append("".join([x if i < y else "_" for i, x in enumerate(z)]))
    for i, x in enumerate(p_lst):
        lst.append(" ".join(x))
    return lst

