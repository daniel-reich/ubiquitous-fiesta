
def major_sum(lst):
  negative=0
  zero=0
  positive=0
  for i in lst:
    if i<0:
      negative=negative+i
    elif i==0:
      zero+=1
    else:
      positive=positive+i
  negative= negative*(-1)
  if negative>zero and negative>positive:
    return negative*(-1)
  elif zero>negative and zero>positive:
    return zero
  else:
    return positive

