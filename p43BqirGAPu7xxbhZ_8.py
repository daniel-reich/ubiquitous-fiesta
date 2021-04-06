
def diamond(carat):
    edge, odd = carat // 2, carat % 2
    edge += odd
    res = [[0] * (edge - 1 - i) + [1] + [0] * i for i in range(edge)]
    res = ([row + row[::-1][1:] for row in res] if odd
           else [row + row[::-1] for row in res])
    res += [row for row in res[::-1][1:]]
    return [res, 'perfect cut' if odd else 'good cut']

