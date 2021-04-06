
def sum_of_holes(n):
    s = ''.join(map(str, range(1, n+1)))
    return s.count('4')+s.count('6')+s.count('8')*2 +s.count('9') + s.count('0')

