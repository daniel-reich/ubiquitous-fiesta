
def slicer(string, slic):
  k = len(string)
  n = string.index(slic[0])
  if len(slic) == 1:
    return "[{}]".format(n)
  m = string.index(slic[-1])
  r = string.index(slic[1]) - n
  if r>1:
    return '[{}:{}:{}]'.format(n if n else '', m+1 if m+r<k else '', r)
  if r==1:
    return '[{}:{}]'.format(n if n else '', m+1 if m+1!=k else '')
  if r<0:
    return '[{}:{}:{}]'.format(n if n!=k-1 else '', m-1 if m+r>=0 else '', r)

