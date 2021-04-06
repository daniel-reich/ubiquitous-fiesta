
def root_digit(n):
  if n//10==0:
    return n
  return root_digit(sum(int(i) for i in str(n)))

