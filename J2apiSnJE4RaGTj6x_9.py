
def find_broken_keys(txt1, txt2):
  seen = []
  seen_add = seen.append
  i=0
  for c in txt1:
    if not c in seen:
      if c!=txt2[i]:
        seen_add(c)
    i+=1
  return seen

