
def bug_jump(h, t):
  t = t/1000
  return [round(t*(2*h**.5-t),2) if t<2*h**.5 else 0, 
        None if t>2*h**.5 else 'up' if t<h**.5 else 'down']

