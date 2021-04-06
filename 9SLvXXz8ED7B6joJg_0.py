
def lets_meet(distance, va, vb):
  t = int(3600*distance/(va+vb))
  return '{}h {}min {}s'.format(t//3600,(t%3600)//60,t%60)

