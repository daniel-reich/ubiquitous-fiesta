
def get_distance(c1, c2):
    x = c2["x"] - c1["x"]
    y = c2["y"] - c1["y"]
    return round((x**2 + y**2)**0.5, 3)

