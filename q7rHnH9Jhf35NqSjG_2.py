
def trailing_zeros(n):
  int_res = 0
  if n < 5:
    return int_res
  i = 1
  while 5**i  < n:
    int_res += n//(5**i)
    i += 1
  return int_res

