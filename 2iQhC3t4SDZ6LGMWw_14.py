
def on_rectangle_bounds(points):
    x_points, y_points = [], []
​
    for i in range(0, len(points)):
        x_points.append(points[i][0])
        y_points.append(points[i][1])
​
    x_max, x_min = max(x_points), min(x_points)
    y_max, y_min = max(y_points), min(y_points)
​
    for i in range(0, len(points)):
        if points[i][0] == x_max or points[i][0] == x_min:
            if y_max >= points[i][1] >= y_min:
                pass
            else:
                return False
        elif points[i][0] != x_max or points[i][0] != x_min:
            if points[i][1] == y_max or points[i][1] == y_min:
                pass
            else:
                return False
​
    return True

