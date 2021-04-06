
def join_digits(n):
  return '-'.join(''.join(str(i) for i in range(1, n+1)))

