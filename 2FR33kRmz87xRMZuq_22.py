
def histogram(lst, char):
  out = []
  for i in lst:
    out.append(i*char)
    out.append('\n')
  return ''.join(out)[:-1]

