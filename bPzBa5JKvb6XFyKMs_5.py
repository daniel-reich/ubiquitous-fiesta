
def get_primiera_score(l):
  d,h,c,s=[],[],[],[]
  for x in l:eval(x[1]).append({'7':21,'6':18,'A':16,'2':12,'3':13,'4':14,'5':15}.get(x[0],10))
  if all((d,h,c,s)):return sum(map(max,(d,h,c,s)))
  return 0

