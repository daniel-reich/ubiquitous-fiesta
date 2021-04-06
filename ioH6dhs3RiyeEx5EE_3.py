
def make_fun_lst(n1, n2):
  return [(lambda k: (lambda x: x*k) if k%2 else (lambda x: x+k))(k) for k in range(n1,n2)]

