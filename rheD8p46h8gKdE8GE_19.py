
def grayscale(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            S = sum([max(0, min(255, g)) for g in lst[i][j]])
            lst[i][j] = [int(round(S / 3.0, 0))] * 3
    return lst

