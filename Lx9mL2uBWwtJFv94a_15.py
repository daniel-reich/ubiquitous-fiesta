
def checker_board(n, el1, el2):
    l = [el1, el2]*n
    return 'invalid' if el1 == el2 else [l[i%2: n+ i%2] for i in range(n)]

