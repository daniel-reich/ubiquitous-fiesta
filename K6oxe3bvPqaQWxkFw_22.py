
def join_digits(n):
  num_str = ''.join(str(i) for i in [i for i in range(1,n+1)])
  return '-'.join(i for i in num_str)

