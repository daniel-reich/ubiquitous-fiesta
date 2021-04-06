
def shortest_path(lst):
    stored, distance = [], 0
    for l,line in enumerate(lst):
        for c,v in enumerate(line):
            if v!= "0":
                stored.append([int(v),l,c])
    if len(stored) < 2:
        return 0
    stored.sort()
    _, s_li, s_co = stored.pop(0)
    for _,li,co in stored:
        distance += abs(s_li-li)+abs(s_co-co)
        s_li, s_co = li, co
    return distance

