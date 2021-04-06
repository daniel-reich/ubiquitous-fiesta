
def verbify(txt):
  t = txt.split() 
  return ' '.join([t[0][:-2]+ t[0][-2:].strip('ed') + 'ed', t[1]])

