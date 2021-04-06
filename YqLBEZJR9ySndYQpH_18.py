
def staircase(n):
    steps = ['_'*(abs(n)-i) + '#'*i for i in range(1, abs(n)+1)]
    return '\n'.join(steps if n > 0 else steps[::-1])

