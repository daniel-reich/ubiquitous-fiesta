
true, false = True, False
# single loop
def get_diagonals(lst):
    d1, d2 = [], []
    for i in range(len(lst)):
        d1.append(lst[i][i])
        d2.append(lst[i][-i-1])
    return [d1, d2]

