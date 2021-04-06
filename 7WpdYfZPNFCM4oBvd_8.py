
allLines = lambda n: [[(r, c) for c in range(n)] for r in range(n)] \
    + [[(i, i) for i in range(n)], [(i, n-i-1) for i in range(n)]]
​
def is_magic(square):
    n = len(square)
    if n == 0: return True
    if n != len(square[0]): return False
    m = n * (n * n +1) // 2
    return all(sum(square[r][c] for r,c in line) == m for line in allLines(n))

