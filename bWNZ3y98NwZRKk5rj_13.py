
def block_player(a, b):
    com = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2), (3, 4, 5), (6, 7, 8),(0, 4, 8), (2, 6, 4)]
    return [j for i in com for j in i if a in i and b in i and j not in (a, b)][0]

