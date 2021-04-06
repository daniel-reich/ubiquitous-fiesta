
def lets_meet(distance, va, vb):
  t = round(distance*3600//(va+vb))
  h, s = t // 3600, t % 3600
  return '{}h {}min {}s'.format(h, s//60, s%60)

