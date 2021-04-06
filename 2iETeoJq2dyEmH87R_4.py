
def count_digits(n, d):
  lst = [str(i ** 2) for i in range(0, n + 1)]
  return sum(1 for i in lst for j in i if j == str(d))

