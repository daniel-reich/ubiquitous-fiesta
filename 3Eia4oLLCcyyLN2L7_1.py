
def remove_repeats(s):
  r = []
  for x in s:
    if not r or r[-1] != x:
      r.append(x)
  return ''.join(r)

