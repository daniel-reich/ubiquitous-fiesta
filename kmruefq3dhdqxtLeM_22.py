
def sum_digits(a, b):
  lst = list(range(a, b+1))
  str_lst = list(map(str, lst))
  h = ''.join(i for i in str_lst)
  return sum([int(j) for j in h])

