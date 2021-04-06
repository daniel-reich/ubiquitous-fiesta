
def join(lst):
    output = ""
    overlap_lst = [0]
    overlap_min = max(list(map(len, lst)))
    for i in range(1,len(lst)):
        overlap = 0
        for j in range(1,len(lst[i-1])):
            if lst[i].startswith(lst[i-1][j:]):
                overlap = len(lst[i-1])-j
                if overlap < overlap_min:
                    overlap_min = overlap
                break
            else:
                continue
        if overlap == 0:
            overlap_min = 0
        overlap_lst.append(overlap)
    for i in range(len(lst)):
        output += lst[i][overlap_lst[i]:]
    return [output, overlap_min]

