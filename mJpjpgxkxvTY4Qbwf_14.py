
def bingo_check(board):
    xs = [(i,j) for i,x in enumerate(board) for j,y in enumerate(x) if y == 'x']
    a = [y for x,y in xs]
    b = [x for x,y in xs]
    return (a.count(a[0]) == 5 or b.count(b[0]) == 5) or all(abs(x[0]-y[0]) == abs(x[1]-y[1]) for x,y in zip(xs, xs[1:]))

