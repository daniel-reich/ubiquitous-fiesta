
def join_digits(n):
  return '-'.join(j for j in (''.join(str(i) for i in range(1, n + 1))))

