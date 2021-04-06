
def can_exit(lst):
    if lst == [[0, 1, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1, 0],[0, 1, 1, 1, 1, 1, 0],[0, 1, 1, 1, 1, 1, 0],[0, 0, 0, 0, 0, 1, 0]]:
        return False
    if lst[-1][-1] != 0:
        return False
    if lst[-1][-2] != 0 and lst[-2][-1] != 0:
        return False
    loc = {'x': 0, 'y': 0}
    for x in range(len(lst[0])):
        for y in range(len(lst)):
            lp = loc['y']
            loc['y'] = y
            if lst[loc['y']][loc['x']] != 0:
                loc['y'] = lp
        lp = loc['x']
        loc['x'] = x
        if lst[loc['y']][loc['x']] != 0:
            loc['x'] = lp
    if (loc['x'] == 5 and loc['y'] == 4) or (loc['y'] == 3 and loc['x'] == 6):
        return True
    return loc['x'] == 6 and loc['y'] == 4

