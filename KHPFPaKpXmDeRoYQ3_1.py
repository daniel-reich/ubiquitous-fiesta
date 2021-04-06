
def check_score(s):
    d = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
    return max(0, sum(d[i] for i in sum(s, [])))

