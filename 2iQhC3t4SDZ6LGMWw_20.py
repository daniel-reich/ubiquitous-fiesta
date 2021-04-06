
def on_rectangle_bounds(dots):
    bounds = [[min(axis), max(axis)] for axis in zip(*dots)]
    return all(map(lambda dot: dot[0] in bounds[0] or dot[1] in bounds[1], dots))

