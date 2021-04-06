
def identify(*cube):
  l = max([len(i) for i in cube])
  m = 0
  for i in cube:
    m+=l-len(i)
  return 'Missing '+str(m) if m else 'Non-Full' if len(cube)<l else 'Full'

