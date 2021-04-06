
def staircase(n, case=0, res=''):
    if case == abs(n):
        return res[:-1]
    if n > 0:
        res += '_' * (n - case - 1) + '#' * (case + 1) + '\n'
    else:
        res += '_' * case + '#' * (-n - case) + '\n'
    return staircase(n, case + 1, res)

