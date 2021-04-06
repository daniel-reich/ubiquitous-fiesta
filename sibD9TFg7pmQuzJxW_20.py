
def sl(n):
  if n<10: return 0,n
  else: return n//10,n%10
​
def dictionary(lst):
  d=dict()
  for i in list(map(sl,lst)):
    if i[0] in d: d[i[0]].append(i[1])
    else: d[i[0]]=[i[1]]
  return d
​
def stem_plot(lst):
  d = dictionary(lst)
  stems = sorted(list(d.keys()))
  return [str(i)+" | "+" ".join(str(j) for j in sorted(d[i])) for i in stems]

