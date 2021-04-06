
def sum_digits(a, b):
  return sum(sum(int(j) for j in list(str(i))) for i in range(a, b+1))

