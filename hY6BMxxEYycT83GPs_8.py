
def multiply_by_11(n):
    num = [0] + list(map(int, list(n)))
    len_res = len(num)
    res = [0] * len_res
    res[-1] = num[-1]
    rem = 0
    for idx in range(len_res - 2, -1, -1):
        rem, ans = divmod(num[idx] + num[idx + 1] + rem, 10)
        res[idx] = ans
    if rem:
        res = [rem] + res
    return "".join(map(str, res))

