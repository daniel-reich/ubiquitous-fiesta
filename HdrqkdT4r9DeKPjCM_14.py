
import numpy as np
​
​
def make_polygonal_numbers(n_rows, n_cols):
    res = np.zeros((n_rows, n_cols), dtype=np.int64)
    for k in range(3, n_rows):
        for i in range(n_cols):
            res[k, i] = k * i * (i + 1) // 2 + 1
            if res[k, i] > n_rows:
                break
    return res
​
​
row_max = 65521
col_max = 106
poly_table = make_polygonal_numbers(row_max, col_max)
​
​
def is_polygonal(n):
    if n == 1:
        return '0th of all'
    elif n not in poly_table:
        return False
    res = []
    for r, c in zip(*np.where(poly_table == n)):
        if c % 10 == 1 and (c < 10 or c > 20):
            res.append('{i}st {k}-gonal number'.format(i=c, k=r))
        elif c % 10 == 2 and (c < 10 or c > 20):
            res.append('{i}nd {k}-gonal number'.format(i=c, k=r))
        elif c % 10 == 3 and (c < 10 or c > 20):
            res.append('{i}rd {k}-gonal number'.format(i=c, k=r))
        else:
            res.append('{i}th {k}-gonal number'.format(i=c, k=r))
    return res

