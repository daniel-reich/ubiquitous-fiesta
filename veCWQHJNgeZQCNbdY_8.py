
def root_digit(n):
  return n if len(str(n))== 1 else root_digit(sum(int(elem) for elem in str(n)))

