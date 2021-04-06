
def make_box(n):
    c1 = ''.join(['#' for i in range(n)])
    c2 = ''.join(['#' if (i == 0 or i == n-1) else ' ' for i in range(n)])
    c3 = [c1 if (i == 0 or i == n-1) else c2 for i in range(n)]
    return c3

