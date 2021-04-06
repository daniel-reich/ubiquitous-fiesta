
def make_fun(k):
  if k % 2:
    return lambda x: x*k
  else:
    return lambda x: x+k
​
def make_fun_lst(n1, n2):
  return [make_fun(k) for k in range(n1, n2)]

