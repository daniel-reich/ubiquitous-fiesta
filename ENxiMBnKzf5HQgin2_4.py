
def pascal_row(n):
    if n < 2:
        return ([1], [1, 1])[n]
    len_res, n_plus_1 = (n + 2 - n % 2) // 2, n + 1
    res = [1] + [0] * (len_res - 1)
    for i in range(1, len_res):
        res[i] = res[i - 1] * (n_plus_1 - i) // i
    return res + res[::-1] if n % 2 else res + res[-2::-1]

