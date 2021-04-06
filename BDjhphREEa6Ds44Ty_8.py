
def bomb(lst):
    for i in lst:
        if i[2] == 0:
            return i[0],i[1]
    d = [0.343 * i[2] for i in lst]
    x1, x2, x3 = lst[0][0], lst[1][0] ,lst[2][0]
    y1, y2, y3 = lst[0][1], lst[1][1] ,lst[2][1]
    k1 = -1 * x1 ** 2 + x2 ** 2 + d[0] ** 2 - d[1] ** 2 - y1 ** 2 + y2 ** 2
    k2 = -1 * x1 ** 2 + x3 ** 2 + d[0] ** 2 - d[2] ** 2 - y1 ** 2 + y3 ** 2
    k3 = 2 * (x2 - x1)
    k4 = 2 * (y2 - y1)
    k5 = 2 * (x3 - x1)
    k6 = 2 * (y3 - y1)
    x_coord = (k1 - k2 * k4 / k6) / (k3 - k5 * k4 / k6)
    if k4 != 0:
        y_coord = (-1 * (k3 * x_coord) + k1) / k4
    else:
        y_coord = (-1 * (k5 *x_coord) + k2) / k6 
    return round(x_coord),round(y_coord)

