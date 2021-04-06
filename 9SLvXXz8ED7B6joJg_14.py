
def lets_meet(distance, va, vb):
  t = distance/(va+vb)
  m = (t - int(t))*60
  s = (m - int(m))*60
  return '{}h {}min {}s'.format(int(t),int(m), int(s))

