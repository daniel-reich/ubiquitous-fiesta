
def staircase(n, h=1):
    ln = abs(n)
    if h == ln:
        return (ln-h)*'_' + h*'#'
    if n  >= 0:
        return (ln-h)*'_' + h*'#' + '\n' + staircase(n, h+1)
    else:
        return staircase(n, h+1) + '\n' + (ln-h)*'_' + h*'#'

