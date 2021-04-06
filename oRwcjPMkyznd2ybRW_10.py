
def max_product(n):
    pairs = []
    for i in range(1, n + 1):
        product = 1
        for c in str(i):
            product *= int(c)
        pairs.append([product, i])
    pairs.sort(reverse=True)
    max_multiplication = pairs[0][0]
    res, idx = [], 0
    while pairs[idx][0] == max_multiplication:
        res.append(pairs[idx][1])
        idx += 1
    return sorted(res)

