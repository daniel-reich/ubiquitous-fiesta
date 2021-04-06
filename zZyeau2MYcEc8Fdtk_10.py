
def round_number(num, n):
  new_n = n
  while new_n < num:
    new_n += n
  return min([new_n, new_n-n], key=lambda x: abs(x-num))

