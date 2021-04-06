
def make_fun_lst(n1, n2):
  def make_sum_func(k):
    sum_func = lambda x: x + k
    return sum_func
  def make_mul_func(k):
    mul_func = lambda x: x * k
    return mul_func
  
  even = lambda n: n%2==0
  tr = []
  
  for k in range(n1, n2):
    if even(k) == True:
      tr.append(make_sum_func(k))
    else:
      tr.append(make_mul_func(k))
  
  return tr

