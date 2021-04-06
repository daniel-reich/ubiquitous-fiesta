
def bug_jump(h, t):
  position = -(t/1000)**2+2*(t/1000)*(h**.5) # position function
  results = [0 if position<0 else round(position, 2)]
  if t/1000>h**.5 and t/1000<2*h**.5 :
    results.append ("down")
  elif t/1000<h**.5 and t/1000>0:
    results.append ("up")
  else :
    results.append (None)
  return results

