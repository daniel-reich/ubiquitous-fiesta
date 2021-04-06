
def longest_slide(p):
    for r in range(1, len(p)):
        for c in range(r + 1):
            if c == 0:
                p[r][c] += p[r - 1][c]
            elif c == r:
                p[r][c] += p[r - 1][c - 1]
            else:
                p[r][c] += max(p[r - 1][c - 1], p[r - 1][c])
    return max(p[-1])

