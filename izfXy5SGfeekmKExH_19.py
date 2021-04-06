
def puzzle_pieces(a1, a2):
    z = []
    if len(a1) != len(a2):
        return False
​
    for x, y in zip(a1, a2):
        z.append(x + y)
    return z.count(z[0]) == len(z)

