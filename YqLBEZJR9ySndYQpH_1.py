
def staircase(n):
  r, k = list(), abs(n)
  for i in range(1, k+1):
    r += [''.join(['_'*(k-i), '#'*i])]
  return '\n'.join([r, r[::-1]][n < 0])

