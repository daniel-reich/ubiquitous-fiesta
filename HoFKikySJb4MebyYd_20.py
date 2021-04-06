
def transform_matrix(lst):
    r, c = len(lst), len(lst[0])
    res = [c * [0] for m in range(r)]
    for i in range(r):
        for j in range(c):
            sum_r_c = 0
            for idx_r in range(c):
                if idx_r != j:
                    sum_r_c += lst[i][idx_r]
            for idx_c in range(r):
                if idx_c != i:
                    sum_r_c += lst[idx_c][j]
            res[i][j] = sum_r_c
    return res

