
def x_and_o(board):
    v, p = [[],[],[]], 0; [v[p].append([1 if i[j]=='X' else -1 if i[j]=='O'
        else 0][0]) for i, p in list(zip(*[board, [0, 1, 2]])) for j in [0, 2, 4]]
    for lin, p in list(zip(*[v, [0, 1, 2]])):
        if sum(lin) == 2: return [p+1, lin.index(0)+1]
    for col, p in list(zip(*[list(zip(*v)), [0, 1, 2]])):
        if sum(col) == 2: return [col.index(0)+1, p+1]
    for diag, p in list(zip(*[[[v[0][0],v[1][1],v[2][2]],[v[0][2],v[1][1],v[2][0]]],[0,1]])):
        if sum(diag) == 2: return [diag.index(0)+1, (diag.index(0))*(1-2*p)+2*p+1]
    return  False

