
def root_digit(n):
  return n if len(str(n)) == 1 else root_digit(sum(int(num) for num in str(n)))

