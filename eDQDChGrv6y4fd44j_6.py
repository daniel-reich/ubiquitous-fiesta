
def can_put(txt, dim):
  ws=txt.split(' ')
  n,m=len(ws),max(map(lambda x: len(x),ws))
  return (n<=dim[0] and m<=dim[1]) or len(txt)<=dim[1]

