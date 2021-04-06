
def seq_level(lst):
    d, level = {1: 'Linear', 2: 'Quadratic', 3: 'Cubic'}, 0
    while len(set(lst)) != 1:
        lst = [a - b for a, b in zip(lst, lst[1:])]
        level += 1
    return d[level]

