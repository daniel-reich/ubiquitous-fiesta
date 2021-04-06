
def Kaprekar(n):
    header = '\n---------- The Mysterious Number 6174 ----------\n\n'
    base = '------------------------------------------------'
​
    if n > 1000 and len(set(str(n))) == 1:
        return header + 'Error, n cannot be a repdigit.\n\n' + base
​
    iterations, i = [], 0
​
    while n != 6174:
        i += 1
        s = ''.join(sorted('{:0>4}'.format(n)))
        n = int(s[::-1]) - int(s)
        iterations.append('Iteration Nr. {}: {} - {} = {:0>4}'.format(i, s[::-1], s, n))
    
    return '{}Number of iterations: {}\n\nIterations:\n\n{}\n\n{}'.format(header, i, '\n'.join(iterations), base)

