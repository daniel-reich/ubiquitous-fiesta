
def reversible_inclusive_list(a,b):
  if a > b:
    return [i for i in range(b,a+1)][::-1]
  else:
    return [i for i in range(a, b+1)]

