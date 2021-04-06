
def is_magic(square):
    if not square:
        return True
    flat = [i for j in square for i in j]
    for i in range(1,max(flat)+1):
        if i not in flat:
            return False
    k = sum(square[0])
    tran = list(map(list,zip(*square)))
    row = [sum(i) == k for i in square]
    col = [sum(i) == k for i in tran]
    diag1 = [sum([square[i][i] for i in range(len(square))]) == k]
    diag2 = [sum([square[i][i] for i in range(len(square[::-1]))]) == k]
    return all(row + col + diag1 + diag2)

