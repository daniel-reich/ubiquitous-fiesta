
def transform_matrix(lst):
    W, H = len(lst[0]), len(lst)
    row_sums = [sum(row) for row in lst]
    lst2 = lst[:]
    col_sums = [sum(row) for row in [list(i) for i in zip(*lst2)]]
    ans = []
    for row in range(H):
        ans_row = []
        for col in range(W):
            ans_row.append(row_sums[row] + col_sums[col] - 2 * lst[row][col])
        ans.append(ans_row)
    return ans

