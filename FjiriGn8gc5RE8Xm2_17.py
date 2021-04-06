
def total_distance(f, fu, p, ac):
  a = (fu+(fu*0.05*p))
  return round((f*100/(a+(0 if not ac else a*0.1))),1)

