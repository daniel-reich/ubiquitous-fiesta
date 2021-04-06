
def record_temps(r, cW):
  temp = []
​
  for d in range(len(cW)):
    dlst = r[d] + cW[d]
    temp.append([min(dlst), max(dlst)])
​
  return temp

