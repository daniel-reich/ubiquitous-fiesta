
def staircase(n):
    res =[]
    for i in range(1,abs(n)+1):
        res.append('_'*(abs(n)-i)+'#'*(i))
    return '\n'.join(res) if n>0 else '\n'.join(res[::-1])

