
def join_digits(n):
  return "-".join([a for y in map(str,range(1, n+1)) for a in y])

