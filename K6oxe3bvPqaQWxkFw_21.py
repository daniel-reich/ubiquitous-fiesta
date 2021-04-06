
def join_digits(n):
  return "-".join("".join(str(i+1) for i in range(n)))

