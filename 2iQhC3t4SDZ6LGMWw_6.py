
def on_rectangle_bounds(points):
    if len(points) < 3:
        return True
    x = []
    y = []
    for i in range(len(points)):
        x.append(points[i][0])
        y.append(points[i][1])
​
    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)
​
    for i in range(len(points)):
        if points[i][0] != xmin:
            if points[i][0] != xmax:
                if points[i][1] != ymin:
                    if points[i][1] != ymax:
                        return False
    return True

