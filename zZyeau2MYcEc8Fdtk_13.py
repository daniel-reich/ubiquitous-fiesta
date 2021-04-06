
def round_number(num, n):
  return [num//n*n, num//n*n+n][num- num//n*n >= num//n*n+n -num]

