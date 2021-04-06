
def staircase(n, lst=[], k=0):
    if k == abs(n):
        return '\n'.join(lst) if n > 0 else '\n'.join(lst[::-1])
    k += 1
    return staircase(n, lst + [('#'*k).rjust(abs(n), '_')], k)

