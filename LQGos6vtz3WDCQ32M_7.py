
def Kaprekar(n):
    ans = ''
    n = str(n)
    if len(n)==4 and len(set(n))==1:
        return '\n---------- The Mysterious Number 6174 ----------\n\nError, n cannot be a repdigit.\n\n------------------------------------------------'
    i = 0
    while n != '6174':
        i += 1
        data = iter(n)
        ans += 'Iteration Nr. {}: {} - {} = {}\n'.format(i, *data)
        n = data[2]
    ans += '\n------------------------------------------------'
    ans = '\n---------- The Mysterious Number 6174 ----------\n' + \
        '\nNumber of iterations: {}\n'.format(i) + \
        '\nIterations:\n\n' + ans
    return ans
​
​
def iter(n):
    fourdigs = sorted('000'+n)[-4:]
    small = ''.join(fourdigs)
    large = ''.join(fourdigs[::-1])
    next = ('000' + str(int(large) - int(small)))[-4:]
    return large, small, next

