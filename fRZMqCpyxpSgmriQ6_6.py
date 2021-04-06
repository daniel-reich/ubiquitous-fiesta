
import string as s 
def sorting(t):
  p3=list(zip(s.ascii_lowercase,s.ascii_uppercase))
  p4=[p3[i][a] for i in range(len(p3)) for a in range(len(p3[i]))]+list(s.digits)
  return ''.join(sorted(t,key=p4.index))

