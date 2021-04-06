
def staircase(n):
    res = ['_'*(n-i-1) + '#'*(i+1) if n > 0 else '_'*i + '#' *
           (abs(n)-i) for i in range(0, abs(n))]
    return ('\n').join(res)

