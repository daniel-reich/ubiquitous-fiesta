
def root_digit(n):
  return n if n < 10 else root_digit(sum(int(d) for d in str(n)))

