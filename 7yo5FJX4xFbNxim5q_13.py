
def harry(lst):
    if lst == [[]]:
        return -1
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                add = lst[i][j - 1]
            elif j == 0:
                add = lst[i - 1][j]
            else:
                add = max(lst[i][j - 1], lst[i - 1][j])
            lst[i][j] += add   
    return lst[len(lst) - 1][len(lst[0]) - 1]

