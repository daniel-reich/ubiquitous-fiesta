
def order_people(lst, people):
    n_rows, n_col = lst
    if n_rows * n_col < people:
        return 'overcrowded'
    sequence = [i if i <= people else 0 for i in range(1, n_rows * n_col + 1)]
    res = []
    for r in range(n_rows):
        if not r % 2:
            res.append(sequence[n_col * r: n_col * (r + 1)])
        else:
            res.append(sequence[n_col * r: n_col * (r + 1)][::-1])
    return res

