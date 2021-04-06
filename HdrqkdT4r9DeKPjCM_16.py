
def is_polygonal(n):
  if n == 1:
    return "0th of all"
  L = []
  for k in range(3,n):
    r = (1+(1+8*(n-1)/k)**(.5))/2
    if r%1 == 0.:
      L += [(int(r)-1,k)]
  if L == []:
    return False
  d = {i:i+"th" for i in "0456789"}
  d["1"], d["2"], d["3"]= "1st", "2nd", "3rd"
  def ord(nstr):
    if int(nstr) not in [11,12,13]:
      return nstr[:-1] + d[nstr[-1]]
    return nstr + "th"
  return [ord(str(r)) + " " + str(k) + "-gonal number" for r,k in L]

