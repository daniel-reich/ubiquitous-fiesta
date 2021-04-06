
def route_diff(directions):
    d = {'N':0, 'S':0, 'E':0, 'W':0}
    for x in directions:
        d[x] += 1
    return len(directions) - abs(d['N'] -d['S']) -abs(d['E'] -d['W'])

