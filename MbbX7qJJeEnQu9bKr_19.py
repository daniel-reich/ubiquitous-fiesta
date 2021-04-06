
def max_occur(text):
  l,c=[],2
  for x in set(text):
    xc=text.count(x)
    if xc==c:
      l.append(x)
    elif xc>c:
      l=[x]
      c=xc
  if not l:
    return "No Repetition"
  return sorted(l)

