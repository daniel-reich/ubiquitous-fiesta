
def pirates_killed(gold, tolerance):
  m=max(gold)
  a=len(gold)
  for i in range(0,a):
    if(m-gold[i]>tolerance[i]):
      return True
  return False

