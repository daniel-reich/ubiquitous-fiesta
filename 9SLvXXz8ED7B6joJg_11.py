
def lets_meet(d, va, vb):
  return '{}h {}min {:0.0f}s'.format(int(d//(va+vb)), int((d%(va+vb)/(va+vb))*60), int(60*(60*d/(va+vb)%1)))

