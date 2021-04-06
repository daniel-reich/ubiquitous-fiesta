
def join_digits(n):
  a = [str(i) for i in range(1, n + 1)]
  b = "".join(a)
  return "-".join(b[x] for x in range(len(b)))

