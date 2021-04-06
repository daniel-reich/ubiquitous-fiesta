
def convert(deg):
  if deg[-1] not in 'FC': return 'Error'
  f = str(round(int(deg[:-2])*1.8+32))+ '*F'
  c = str(round((int(deg[:-2])-32)/1.8))+ '*C'
  return f if deg[-1]=='C' else c

