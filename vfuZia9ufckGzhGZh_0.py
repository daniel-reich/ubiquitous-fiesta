
def seq_level(lst):
  seq = lambda x:[b-a for a,b in zip(x,x[1:])]
  is_linear = lambda x:len(set(seq(x))) == 1
  
  return 'Linear' if is_linear(lst)\
    else 'Quadratic' if is_linear(seq(lst))\
    else 'Cubic'

