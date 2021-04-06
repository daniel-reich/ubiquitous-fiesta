
def fibFast(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibFast(n-1, computed) + fibFast(n-2, computed)
    return computed[n]

