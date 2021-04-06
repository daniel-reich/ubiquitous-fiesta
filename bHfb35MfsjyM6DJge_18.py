
def route_diff(directions):
    f = lambda a, b: abs(directions.count(a) - directions.count(b))
    return len(directions) - (f("N", "S") + f("W", "E"))

