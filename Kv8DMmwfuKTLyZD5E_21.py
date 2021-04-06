
def make_dartboard(n):
    if n % 2:
        res = [[n // 2 + 1]]
    else:
        center = n // 2
        res = [[center, center], [center, center]]
    while res[0][0] > 1:
        edge = res[0][0] - 1
        res = [[edge] * (len(res) + 2)] + res + [[edge] * (len(res) + 2)]
        for i in range(1, len(res) - 1):
            res[i] = [edge] + res[i] + [edge]
    return [int(''.join(str(i) for i in row)) for row in res]

