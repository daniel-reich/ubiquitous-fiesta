
def alpha_range(start, stop, step=1):
  a = 'abcdefghijklmnopqrstuvwxyz'
  if start.islower()==stop.islower() and step!=0 and -26<step<26:
    if start.isupper():
      a = a.upper()
    if step>0: return [a[i] for i in range(min(a.index(start),a.index(stop)),max(a.index(stop),a.index(start))+1,step)]
    else: return [a[i] for i in range(max(a.index(start),a.index(stop)),min(a.index(start),a.index(stop))-1,step)]
  elif start.islower()!=stop.islower():
    return "both start and stop must share the same case"
  else:
    return "step must be a non-zero value between -26 and 26, exclusive"

