
def is_repdigit(num):
  return all(str(num)[0] == i for i in str(num))

