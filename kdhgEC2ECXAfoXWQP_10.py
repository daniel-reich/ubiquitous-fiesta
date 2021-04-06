
def transpose_matrix(mtx):
    flag_range = 0
    flag = 0
    lst = []
    for i in range(len(mtx)*len(mtx[0])):
        lst.append(mtx[flag][flag_range])
        flag += 1
        if flag == len(mtx) and len(mtx[0]) > 1:
            flag_range += 1
            flag = 0
    return ' '.join(lst)

