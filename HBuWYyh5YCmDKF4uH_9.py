
def almost_sorted(lst):
    count = 0
    c = 0
    for a in range(0, len(lst) - 1):
        if lst[a] > lst[a + 1]:
            count += 1
    if count != 1:
        for b in range(0 , len(lst) -1):
            if lst[b] < lst[b+1]:
                c += 1
    if c == 1 or count == 1:
        return True
    return False

