
def is_repdigit(num):
  x = str(num)
  return all(i == x[0] for i in str(num))

