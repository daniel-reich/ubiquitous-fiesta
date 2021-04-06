
def on_rectangle_bounds(points):
    x_vals, y_vals = zip(*points)
    x1, x2, y1, y2 = min(x_vals), max(x_vals), min(y_vals), max(y_vals)
    return all(x in (x1, x2) and y1<=y<=y2 or y in (y1, y2) and x1<=x<=x2 for x, y in points)

