
def is_repdigit(num):
  return all(d == str(num)[0] for d in str(num))

