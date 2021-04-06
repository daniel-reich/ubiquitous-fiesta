
def diamond_sum(n):
    total = 0
    diamond_list = []
    row = []
    if n == 1:
        return 1
    for i in range(1, n*n + 1):
        row.append(i)
        if len(row) == n:
            diamond_list.append(row)
            row = []
    top_number = diamond_list[0][(n - 1)//2]
    bottom_number = diamond_list[n - 1][(n - 1)//2]
    total += top_number + bottom_number
    margin = 1
    for j in range(1, ((n - 1)//2)):
        total += diamond_list[j][((n - 1)//2) - margin] + diamond_list[j][((n - 1)//2) + margin]
        margin += 1
    total += diamond_list[(n - 1)//2][0] + diamond_list[(n - 1)//2][n - 1]
    new_margin = 1
    for k in range((((n - 1)//2) + 1), n - 1):
        total += diamond_list[k][0 + new_margin] + diamond_list[k][(n - 1) - new_margin]
        new_margin += 1
    return total

