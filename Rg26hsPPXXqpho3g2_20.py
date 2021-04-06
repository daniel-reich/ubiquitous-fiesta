
def which_is_larger(f, g):
  if f() == g(): return 'neither'
  if f() > g(): return 'f'
  if g() > f(): return 'g'

