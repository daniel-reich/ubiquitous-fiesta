
def which_is_larger(f, g):
  return ['f','g'][f()<g()] if f()!=g()else 'neither'

