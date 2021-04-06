
def on_rectangle_bounds(points):
    x = [i[0] for i in points]
    y = [i[1] for i in points]
    x = [min(x), max(x)]
    y = [min(y), max(y)]
    
    if len(set(x)) == 1 or len(set(y)) == 1:
        return True
    return all(([i[0] in x or i[1] in y for i in points]))

