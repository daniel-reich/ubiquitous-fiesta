
def split_code(item):
  l=list()
  n=''
  for i in range(len(item)):
    if item[i] in '0123456789':
      n=item[i:]
      break
    else:
      l.append(item[i])
  return [''.join(l),int(n)]

