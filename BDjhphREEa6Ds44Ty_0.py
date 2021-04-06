
def bomb(lst):
    a = lst[0][2] * 0.343
    b = lst[1][2] * 0.343
    c = lst[2][2] * 0.343
    if a == b == c == 0:
        return lst[0][0], lst[0][1]
    a1 = 2 * (lst[1][0] - lst[0][0])
    b1 = 2 * (lst[1][1] - lst[0][1])
    d1 = 2 * (lst[2][0] - lst[0][0])
    e1 = 2 * (lst[2][1] - lst[0][1])
    c1 = (a * a - b * b - lst[0][0] ** 2 + lst[1][0] ** 2
          - lst[0][1] ** 2 + lst[1][1] ** 2)
    f1 = (a * a - c * c - lst[0][0] ** 2 + lst[2][0] ** 2
          - lst[0][1] ** 2 + lst[2][1] ** 2)
    x = (c1 - f1 * b1 / e1) / (a1 - d1 * b1 / e1)
    if b1 == 0:
        y = (f1 - x * d1) / e1
    else:
        y = (c1 - x * a1) / b1
    return round(x), round(y)

