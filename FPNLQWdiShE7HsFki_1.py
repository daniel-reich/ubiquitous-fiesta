
from math import sin, pi
inner_edge = [i * 2 * sin(pi / 8) for i in range(5)]
grid = "ABCDEFGH"
​
def spider_vs_fly(spider, fly):
    s_radial, s_radius = spider[0], int(spider[1])
    f_radial, f_radius = fly[0], int(fly[1])
    s_idx = grid.index(s_radial)
    clockwise = 0
    while grid[(s_idx + clockwise) % 8] != f_radial:
        clockwise += 1
    counterwise = 0
    while grid[(s_idx - counterwise) % 8] != f_radial:
        counterwise += 1
    h_distance = min(clockwise, counterwise)
    direction = clockwise <= counterwise
    via_center = s_radius + f_radius
    min_r = min(s_radius, f_radius)
    via_edge = (abs(s_radius - min_r) + abs(f_radius - min_r)
                + h_distance * inner_edge[min_r])
    if via_center <= via_edge:
        return ("-".join("{}{}".format(s_radial, i)
                         for i in range(s_radius, 0, -1)) + "-A0-" +
                "-".join("{}{}".format(f_radial, i)
                         for i in range(1, f_radius + 1)))
    elif s_radius > min_r:
        res = "-".join("{}{}".format(s_radial, i)
                       for i in range(s_radius, min_r - 1, -1))
        if h_distance > 0:
            res += "-"
            res += "-".join("{}{}".format(grid[(s_idx +
                                                (step if direction else -step))
                                               % 8], str(min_r))
                            for step in range(1, h_distance + 1))
    else:
        res = "-".join("{}{}".format(grid[(s_idx +
                                          (step if direction else -step))
                                          % 8], str(min_r))
                       for step in range(h_distance + 1))
        if f_radius > min_r:
            res += "-"
            res += "-".join("{}{}".format(f_radial, i)
                            for i in range(min_r + 1, f_radius + 1))
    return res

