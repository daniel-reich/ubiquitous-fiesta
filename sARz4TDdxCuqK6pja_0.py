
def deadly_virus(persons, n):
    A = {(r, c):v for r, row in enumerate(persons) for c, v in enumerate(row)}
    for _ in range(n):
        for n in {(r, c) for r, c in A if any(A.get((r+rr, c+cc), '') == 'V' for rr, cc in [(1, 0), (-1, 0), (0, 1), (0,-1)])}:
            A[n] = 'V'
     
    return [[A[(r, c)] for c in range(len(persons[0]))] for r in range(len(persons))]

