
def is_wristband(lst):
    rows = all(len(set(row)) == 1 for row in lst)
    cols = all(len(set(col)) == 1 for col in list(map(list,zip(*lst))))
    diag1 = all(len(set(diag)) == 1 for diag in [[row[i-j] for i,row in enumerate(lst) if 0 <= i-j < len(row)] for j in range(-len(lst[0])+1,len(lst))])
    diag2 = all(len(set(diag)) == 1 for diag in [[row[j-i] for i,row in enumerate(lst) if 0 <= j-i < len(row)] for j in range(len(lst[0])+len(lst)-1)])
    return any([rows,cols,diag1,diag2])

