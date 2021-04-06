
def super_digit(n, k=1):
  if len(n) == 1:
    return sum([int(i) for i in n*k])
  else:
    return super_digit(str(sum([int(i) for i in n*k])))

