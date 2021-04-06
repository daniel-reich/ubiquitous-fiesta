
def count_towers(towers):
    lst = []
    if towers == []:
        return 0
    for i in towers[-1][0]:
        if i == "#":
            lst.append(i)
    return int(len(lst)/2)

