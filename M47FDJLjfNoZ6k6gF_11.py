
def cup_swapping(s, t="B"):
  for _, a in enumerate(s): t = a.replace(t, "") if t in a else t  
  return t

