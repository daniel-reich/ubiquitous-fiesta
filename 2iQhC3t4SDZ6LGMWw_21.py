
def on_rectangle_bounds(points):
    len_points = len(points)
    x, y = [0] * len_points, [0] * len_points
    for i in range(len_points):
        x[i], y[i] = points[i][0], points[i][1]
    x_min, x_max, y_min, y_max = min(x), max(x), min(y), max(y)
    for i in range(len_points):
        if not (((points[i][0] == x_min or points[i][0] == x_max)
                and y_min <= points[i][1] <= y_max) or
                ((points[i][1] == y_min or points[i][1] == y_max)
                 and x_min <= points[i][0] <= x_max)):
            return False
    return True

