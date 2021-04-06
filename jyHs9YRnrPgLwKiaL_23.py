
def split(x):
  s=[1]
  for a in range(1,int(x/2)+1):
    s.append(round((x/a)**a,1))
  return max(s)

