
def is_polygonal(n):
  if n==1:
    return "0th of all"
  if n <= 3:
    return False
  list = []
  for k in range(3, n):
    i=1
    current=k+1
    while current < n:
      i+=1
      current += k*i
    if current == n:
      i = str(i)
      i += "th" if i[-2:-1]=="1" else {"1":"st","2":"nd","3":"rd"}.get(i[-1],"th")
      list.append("{ith} {k}-gonal number".format(ith=i,k=k))
  return list

