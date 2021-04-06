
def count_towers(towers):
    k = []
    for i in towers:
        j = i[0].split()
        le = len(j)
        k.append(le)
    return max(k)

