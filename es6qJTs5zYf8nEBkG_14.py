
def unpack(point):
    return tuple([int(_) for _ in point.replace('(', '').replace(')', '').split(',')])
​
def is_rectangle(coordinates):
    if len(coordinates) != 4:
        return False
    coords = []
    for c in coordinates:
        coords.append(unpack(c))
    coords.sort()
    if len(set(coords)) != 4:
        return False
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    x3, y3 = coords[2]
    x4, y4 = coords[3]
    return x1 == x2 and x3 == x4 and y1 == y3 and y2 == y4

