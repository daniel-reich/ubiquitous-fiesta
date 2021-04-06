
def divisible_by_left(n):
  x = '0' + str(n)
  return [int(x[i + 1]) % int(x[i]) == 0 if int(x[i]) != 0 else False for i in range(len(x) - 1)]

