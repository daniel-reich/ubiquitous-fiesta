
def staircase(n):
    if n == 1 or n == -1: return '#'
    if n < -1:
        lst = staircase(n+1).split('\n')
        for a, b in enumerate(lst): lst[a] = (abs(n) - len(b)) * '_' + b
        lst.insert(0, '#' * abs(n))
    if n > 1:
        lst = staircase(n-1).split('\n')
        for a, b in enumerate(lst): lst[a] = (abs(n) - len(b)) * '_' + b
        lst.append('#' * abs(n))
    return '\n'.join(lst)

