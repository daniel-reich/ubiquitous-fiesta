
def mystery_func(x):
  return ''.join([x[i - 1] * int(x[i]) for i in range(len(x)) if x[i].isdigit()])

