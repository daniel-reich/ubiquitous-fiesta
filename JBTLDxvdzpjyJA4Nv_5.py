
def super_reduced_string(txt):
  q= []
  for c in txt:
    if q and c == q[-1]:
      q.pop()
    else:
      q.append(c)
  return ''.join(q) if q else 'Empty String'

