
def two_product(a, n):
    if max(a) < int(pow(n, 0.5)):
        return None
    lst_res = []
    for i in range(1, len(a)):
        for j in range(1, max(i, len(a) - i)):
            if i - j >= 0 and a[i - j] * a[i] == n:
                res = [a[i - j], a[i]]
                if res not in lst_res:
                    lst_res.append(res)
            if i + j < len(a) and a[i] * a[i + j] == n:
                res = [a[i], a[i + j]]
                if res not in lst_res:
                    lst_res.append([a[i], a[i + j]])
    return lst_res[0] if len(lst_res) == 1 else lst_res[2]

