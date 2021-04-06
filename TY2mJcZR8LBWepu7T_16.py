
def risiko(a,d):
  a.sort(reverse=True)
  d.sort(reverse=True)
  comparisons = min(len(a),len(d))
  d_loses = 0
  
  for i in range(comparisons):
    if a[i] > d[i]: d_loses += 1
  return d_loses

