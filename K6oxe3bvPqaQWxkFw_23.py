
def join_digits(n):
  return "-".join(list("".join(map(str, range(1, n + 1)))))

