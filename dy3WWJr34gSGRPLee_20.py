
def make_box(n):
    return ['#' * n if i == 1 or i == n else '#' + ' ' * (n-2) + '#' for i in range(1,n+1)]

