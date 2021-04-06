
def hours_passed(time1, time2):
  if time1==time2:
    return "no time passed"
  [t1,m1],[t2,m2]=time1.split(),time2.split()
  h1,h2=map(int,[t1[0],t2[0]])
  if m1!=m2:
    h=h2-h1+12
  else:
    h=(h2-h1+24)%24
  return "{} hours".format(h)

