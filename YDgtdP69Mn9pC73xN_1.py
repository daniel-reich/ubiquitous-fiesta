
def num_grid(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == '#':
                continue
            lst[i][j] = str(sum(lst[k][l] == '#' for k in range(len(lst)) for l in range(len(lst[0]))
                            if abs(i - k) < 2 and abs(j - l) < 2))
    return lst

