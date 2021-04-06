
def make_rug(m, n, *s):
    if s:
        return [''.join(s * n) for _ in range(m)]
    else:
        return ['#' * n for _ in range(m)]

