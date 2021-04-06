
def first_and_last(s):
  res = []
  res.append(''.join(sorted(s)))
  res.append(''.join((sorted(s, reverse=True))))
  
  return res

