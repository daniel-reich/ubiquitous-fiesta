
def sig_figs(num):
  s = num.lstrip('-0.')
  if not '.' in num:
    s = s.rstrip('0')
  else:
    s = s.replace('.','')
  return len(s)

