
output = ['\n---------- The Mysterious Number 6174 ----------\n', 
          '\n------------------------------------------------']
​
def Kaprekar(n):
    ns = str(n).zfill(4)
    if len(set(ns)) == 1:
        return output[0] + '\nError, n cannot be a repdigit.\n' + output[1]
    iterations = []
    while n != 6174:
        digits = sorted(list(str(n).zfill(4)))
        mn, mx = int(''.join(digits)), int(''.join(digits[::-1]))
        n = mx - mn
        iterations.append('Iteration Nr. {}: {:04} - {:04} = {:04}\n'.format(len(iterations)+1, mx, mn, n))
    return output[0] + \
        '\nNumber of iterations: {}\n'.format(len(iterations)) + \
        '\nIterations:\n' + \
        '\n' + ''.join(iterations) + output[1]

