
def f(area, c):
    dis2 = (pow(c, 4) - 16 * area * area)
    if dis2 < 0:
        return "Does not exist"
    a = pow((c * c + pow(dis2, 0.5)) / 2, 0.5)
    b = 2 * area / a
    return [round(b, 3), round(a, 3)]

