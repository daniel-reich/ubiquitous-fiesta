
def Kaprekar(n):
    n = str(n)
    if len(n) == 4 and all(n[i] == n[i+1] for i in range(len(n)-1)):
        return '\n---------- The Mysterious Number 6174 ----------\n\nError, n cannot be a repdigit.\n\n------------------------------------------------'
    i = 1
    r = '\nIterations:\n\n'
    while n!= 6174:
        n = str(n)
        n1, n2 = ''.join(sorted(n)), ''.join(sorted(n)[::-1])
        n1 = (4-len(n1))*'0'+n1
        n2 = n2+(4-len(n2))*'0'
        n = int(n2) - int(n1)
        r += 'Iteration Nr. '+str(i)+': '+n2+' - '+n1+' = '+ (4-len(str(n)))*'0'+str(n)+'\n'
        i += 1
​
    return '\n---------- The Mysterious Number 6174 ----------\n' \
        '\nNumber of iterations: {}\n'.format(i-1) + r + \
        '\n------------------------------------------------'

